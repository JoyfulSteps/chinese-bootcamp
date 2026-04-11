#!/usr/bin/env python3
"""
grammar_sync.py
───────────────
Sync grammar cards từ grammar_output/grammar_cards.json vào Anki
qua AnkiConnect (http://127.0.0.1:8766).

Deck đích: Chinese Grammar
Note Type: Chinese Grammar Card

Usage:
    python grammar_sync.py                  # sync tất cả
    python grammar_sync.py --week 1         # chỉ week 1
    python grammar_sync.py --dry-run        # xem trước, không ghi
    python grammar_sync.py --update-template # cập nhật template thẻ
    python grammar_sync.py --rebuild        # xóa và tạo lại toàn bộ
"""

import json
import sys
import os
import re
import urllib.request
import urllib.error
from pathlib import Path

# ─── Config ──────────────────────────────────────────────────────────────────

ANKI_CONNECT_URL = "http://127.0.0.1:8766"
ANKI_CONNECT_VER = 6

BASE_DIR     = Path(__file__).parent
JSON_PATH    = BASE_DIR / "grammar_output" / "grammar_cards.json"
CARD_DIR     = BASE_DIR / "grammar_card"

DECK_NAME    = "Chinese Grammar"
MODEL_NAME   = "Chinese Grammar Card"

# Sub-decks theo tuần
SUBDECK_PATTERN = "Chinese Grammar::Week {}"   # e.g. Chinese Grammar::Week 1

# Fields phải khớp với Note Type trong Anki
FIELD_NAMES = [
    "NoteID",
    "GrammarName",
    "GrammarMeaning",
    "Pattern",
    "Examples",
    "Notes",
    "DevTip",
    "Exercise",
    "Day",
    "Week",
    "SourceFile",
    "Tags",
]

# ─── Args ────────────────────────────────────────────────────────────────────

DRY_RUN          = "--dry-run"        in sys.argv
UPDATE_TEMPLATE  = "--update-template" in sys.argv
REBUILD          = "--rebuild"        in sys.argv
WEEK_FILTER      = None

for i, arg in enumerate(sys.argv):
    if arg == "--week" and i + 1 < len(sys.argv):
        try: WEEK_FILTER = int(sys.argv[i + 1])
        except: pass

# ─── AnkiConnect Helper ──────────────────────────────────────────────────────

def anki(action: str, **params):
    """Send a request to AnkiConnect. Returns result or raises."""
    payload = json.dumps({
        "action": action,
        "version": ANKI_CONNECT_VER,
        "params": params,
    }).encode()
    try:
        req  = urllib.request.Request(ANKI_CONNECT_URL, payload)
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())
    except urllib.error.URLError:
        print("\n❌ Không kết nối được AnkiConnect!")
        print("   → Mở Anki trước, cài add-on AnkiConnect (2055492159)")
        sys.exit(1)

    if data.get("error"):
        raise RuntimeError(f"AnkiConnect error: {data['error']}")
    return data["result"]


def anki_safe(action: str, **params):
    """Gọi anki() nhưng bắt lỗi, trả về None nếu fail."""
    try:
        return anki(action, **params)
    except RuntimeError as e:
        return None

# ─── Template ────────────────────────────────────────────────────────────────

def read_template(name: str) -> str:
    path = CARD_DIR / name
    if not path.exists():
        print(f"⚠️  Template không tồn tại: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def ensure_model():
    """Tạo Note Type nếu chưa có; cập nhật template nếu cần."""
    model_names = anki("modelNames")

    front_html = read_template("front.html")
    back_html  = read_template("back.html")
    css        = read_template("style.css")

    if MODEL_NAME not in model_names:
        print(f"📋 Tạo mới Note Type: {MODEL_NAME}")
        if not DRY_RUN:
            anki("createModel",
                modelName   = MODEL_NAME,
                inOrderFields = FIELD_NAMES,
                css         = css,
                cardTemplates = [{
                    "Name":  "Grammar Card",
                    "Front": front_html,
                    "Back":  back_html,
                }]
            )
        print("   ✅ Done")
    else:
        if UPDATE_TEMPLATE or REBUILD:
            print(f"🔄 Cập nhật template: {MODEL_NAME}")
            if not DRY_RUN:
                # Update CSS
                anki("updateModelStyling",
                    model={"name": MODEL_NAME, "css": css})
                # Update templates
                anki("updateModelTemplates",
                    model={
                        "name": MODEL_NAME,
                        "templates": {
                            "Grammar Card": {
                                "Front": front_html,
                                "Back":  back_html,
                            }
                        }
                    }
                )
            print("   ✅ Template updated")
        else:
            print(f"✅ Note Type đã tồn tại: {MODEL_NAME}")


def ensure_decks(cards: list):
    """Tạo parent deck + sub-decks theo tuần."""
    weeks = set(c["week_num"] for c in cards)
    if not DRY_RUN:
        anki("createDeck", deck=DECK_NAME)
        for w in sorted(weeks):
            anki("createDeck", deck=SUBDECK_PATTERN.format(w))
    else:
        print(f"[DRY] Sẽ tạo deck: {DECK_NAME} + {len(weeks)} sub-decks")

# ─── Card Operations ─────────────────────────────────────────────────────────

def card_to_fields(card: dict) -> dict:
    """Chuyển dict card → dict fields Anki."""
    return {
        "NoteID":         card.get("note_id", ""),
        "GrammarName":    card.get("grammar_name", ""),
        "GrammarMeaning": card.get("grammar_meaning", ""),
        "Pattern":        card.get("pattern", ""),
        "Examples":       card.get("examples", ""),
        "Notes":          card.get("notes", ""),
        "DevTip":         card.get("dev_tip", ""),
        "Exercise":       card.get("exercise", ""),
        "Day":            card.get("day", ""),
        "Week":           card.get("week", ""),
        "SourceFile":     card.get("source_file", ""),
        "Tags":           card.get("tags", ""),
    }


def build_tags(card: dict) -> list:
    """Build Anki tag list từ tags string."""
    raw = card.get("tags", "")
    tags = [t.replace("::", "::") for t in raw.split("::") if t]
    tags.append("grammar")
    return list(set(tags))


def find_existing_note(note_id: str, grammar_name: str):
    """Tìm note đã có bằng NoteID trước, fallback sang GrammarName."""
    # Ưu tiên dùng NoteID (ổn định hơn)
    if note_id:
        notes = anki_safe("findNotes",
            query=f'"note:{MODEL_NAME}" NoteID:{note_id}'
        )
        if notes:
            return notes[0]
    # Fallback: tìm theo GrammarName (cho các note cũ chưa có NoteID)
    escaped = grammar_name.replace('"', '\\"')
    notes = anki_safe("findNotes",
        query=f'"note:{MODEL_NAME}" GrammarName:"{escaped}"'
    )
    return notes[0] if notes else None


def rebuild_clean():
    """Xóa toàn bộ cards cũ trong deck (chỉ dùng khi --rebuild)."""
    print("🗑️  Đang xóa toàn bộ cards cũ...")
    note_ids = anki_safe("findNotes", query=f'"note:{MODEL_NAME}"') or []
    if note_ids and not DRY_RUN:
        anki("deleteNotes", notes=note_ids)
    print(f"   Đã xóa {len(note_ids)} notes cũ")


def sync_card(card: dict) -> str:
    """Sync 1 card. Returns 'created' | 'updated' | 'skipped'."""
    grammar_name = card.get("grammar_name", "")
    note_id      = card.get("note_id", "")
    week_num     = card.get("week_num", 1)
    deck         = SUBDECK_PATTERN.format(week_num)
    fields       = card_to_fields(card)
    tags         = build_tags(card)

    # Check existing
    existing = find_existing_note(note_id, grammar_name) if not REBUILD else None

    if existing:
        # Update
        if not DRY_RUN:
            anki("updateNoteFields", note={
                "id": existing,
                "fields": fields,
            })
            anki("updateNoteTags", note=existing, tags=" ".join(tags))
            # Move to correct deck
            card_ids = anki("notesInfo", notes=[existing])
            if card_ids:
                for info in card_ids:
                    for cid in info.get("cards", []):
                        anki("changeDeck", cards=[cid], deck=deck)
        return "updated"

    else:
        # Create new
        note = {
            "deckName":  deck,
            "modelName": MODEL_NAME,
            "fields":    fields,
            "tags":      tags,
            "options":   {"allowDuplicate": False, "duplicateScope": "deck"},
        }
        if not DRY_RUN:
            anki("addNote", note=note)
        return "created"

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  Chinese Grammar → Anki Sync")
    print("=" * 55)

    if DRY_RUN:
        print("  [DRY-RUN mode — không thay đổi Anki]\n")

    # Load data
    if not JSON_PATH.exists():
        print(f"❌ Không tìm thấy: {JSON_PATH}")
        print("   Hãy chạy grammar_extract.py trước!")
        sys.exit(1)

    all_cards = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    print(f"📦 Loaded {len(all_cards)} grammar cards\n")

    # Filter
    cards = all_cards
    if WEEK_FILTER is not None:
        cards = [c for c in cards if c.get("week_num") == WEEK_FILTER]
        print(f"🔍 Filter: Week {WEEK_FILTER} → {len(cards)} cards\n")

    if not cards:
        print("⚠️  Không có card nào để sync.")
        return

    # Setup
    ensure_model()
    ensure_decks(cards)

    if REBUILD and not DRY_RUN:
        rebuild_clean()

    print(f"\n🔄 Syncing {len(cards)} cards...\n")

    created = updated = skipped = errors = 0

    for i, card in enumerate(cards, 1):
        name = card.get("grammar_name", f"Card {i}")
        try:
            result = sync_card(card)
            icon = "✅" if result == "created" else "🔄" if result == "updated" else "⏭️"
            print(f"  {icon} [{i:2d}/{len(cards)}] {name}  ({result})")
            if result == "created": created += 1
            elif result == "updated": updated += 1
            else: skipped += 1
        except Exception as e:
            print(f"  ❌ [{i:2d}/{len(cards)}] {name}  ERROR: {e}")
            errors += 1

    # Sync collection
    if not DRY_RUN:
        anki_safe("sync")

    print("\n" + "=" * 55)
    print(f"  ✅ Created : {created}")
    print(f"  🔄 Updated : {updated}")
    print(f"  ⏭️  Skipped : {skipped}")
    if errors:
        print(f"  ❌ Errors  : {errors}")
    print("=" * 55)

    if not DRY_RUN and (created + updated) > 0:
        print(f"\n🎉 Kiểm tra Anki deck: «{DECK_NAME}»")
        if UPDATE_TEMPLATE:
            print("🎨 Template đã được cập nhật!")
    print()


if __name__ == "__main__":
    main()
