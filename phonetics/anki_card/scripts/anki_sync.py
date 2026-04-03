"""
Anki Chinese Vocab Sync
Parse AI-generated .md files -> sync with Anki via AnkiConnect.

Usage:
    python scripts/anki_sync.py --day "Day 1" --input-dir ./output
    python scripts/anki_sync.py --day "Day 1" --words "我,你,他"

Cards are identified by Card_Number (md5 hash of Hanzi).
Re-running will UPDATE existing cards instead of duplicating.
"""

import sys
import json
import re
import hashlib
import argparse
import urllib.request
from pathlib import Path

# ══════════════════════════════════
# CONFIG
# ══════════════════════════════════
ANKI_URL = "http://localhost:8765"
SOURCE_DECK = "Mandarin: Vocabulary::a. HSK"
TARGET_DECK_PREFIX = "Chinese Foundation"


def anki_request(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params})
    req = urllib.request.Request(ANKI_URL, data=payload.encode("utf-8"))
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"[ERR] Khong ket noi duoc Anki: {e}")
        sys.exit(1)
    if result.get("error"):
        raise Exception(result["error"])
    return result.get("result")


def generate_card_id(hanzi):
    """Stable unique ID from Hanzi (md5 short hash)."""
    return hashlib.md5(hanzi.encode("utf-8")).hexdigest()[:8].upper()


# ============================================================
# Markdown to HTML
# ============================================================

def inline(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def md_to_html(md_text):
    lines = md_text.strip().split("\n")
    html_parts = []
    in_table = False
    in_list = False
    table_rows = []

    def is_sep(cells):
        return all(re.match(r'^[:\-\s]+$', c) for c in cells)

    def flush_table():
        nonlocal table_rows, in_table
        if not table_rows:
            return ""
        header = table_rows[0]
        remaining = table_rows[1:]
        if remaining and is_sep(remaining[0]):
            remaining = remaining[1:]
        out = "<table><thead><tr>"
        for c in header:
            out += f"<th>{inline(c.strip())}</th>"
        out += "</tr></thead><tbody>"
        for row in remaining:
            out += "<tr>"
            for c in row:
                out += f"<td>{inline(c.strip())}</td>"
            out += "</tr>"
        out += "</tbody></table>"
        table_rows = []
        in_table = False
        return out

    for line in lines:
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            in_table = True
            cells = [c for c in s.split("|")[1:-1]]
            table_rows.append(cells)
            continue
        elif in_table:
            html_parts.append(flush_table())
        if re.match(r"^[-*] ", s):
            content = inline(s[2:])
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            html_parts.append(f"<li>{content}</li>")
            continue
        elif in_list:
            html_parts.append("</ul>")
            in_list = False
        if not s:
            continue
        html_parts.append(f"<p>{inline(s)}</p>")

    if in_table:
        html_parts.append(flush_table())
    if in_list:
        html_parts.append("</ul>")
    return "\n".join(html_parts)


# ============================================================
# Parse .md file
# ============================================================

def parse_md(filepath):
    text = Path(filepath).read_text(encoding="utf-8")
    result = {
        "illustrate_word": "",
        "stroke_order": "",
        "stroke_summary": "",
        "hint_front": "",
        "meta": {}
    }
    parts = re.split(r'---(STROKE_ORDER|STROKE_SUMMARY|HINT_FRONT|META)---', text)
    result["illustrate_word"] = parts[0].strip()
    i = 1
    while i < len(parts) - 1:
        key = parts[i].strip().lower()
        val = parts[i + 1].strip()
        if key == "stroke_order":
            result["stroke_order"] = val
        elif key == "stroke_summary":
            result["stroke_summary"] = val
        elif key == "hint_front":
            result["hint_front"] = val
        elif key == "meta":
            for line in val.split("\n"):
                line = line.strip()
                if ": " in line:
                    k, v = line.split(": ", 1)
                    result["meta"][k.strip()] = v.strip()
        i += 2
    return result


# ============================================================
# Build ALL fields from parsed .md data
# ============================================================

def build_fields(data):
    """Build complete field dict from parsed .md data."""
    meta = data["meta"]
    hanzi = meta.get("Hanzi", "")
    card_id = generate_card_id(hanzi)

    fields = {
        # Key field
        "Card_Number": card_id,
        # META fields - always overwrite
        "Hanzi": hanzi,
        "Pinyin": meta.get("Pinyin", ""),
        "Meaning_VN_Short": meta.get("Meaning_VN_Short", ""),
        "Part_of_Speech": meta.get("Part_of_Speech", ""),
        "HSK_Level": f"HSK{meta.get('HSK', '')}",
        "Meaning": meta.get("Meaning_EN", ""),
        "Pinyin.2": meta.get("Pinyin_Num", ""),
        # AI-generated fields - always overwrite
        "Illustrate_Word": md_to_html(data["illustrate_word"]),
        "Stroke_Order": md_to_html(data["stroke_order"]),
        "Stroke_Summary": data["stroke_summary"],
        "Hint_Front": data["hint_front"],
    }

    # Optional sentence fields (only set if provided, don't erase existing)
    if meta.get("Sentence_ZH"):
        fields["Sentence_ZH"] = meta["Sentence_ZH"]
    if meta.get("Sentence_EN"):
        fields["Sentence_EN"] = meta["Sentence_EN"]

    return fields


# ============================================================
# Find note by Hanzi or Card_Number
# ============================================================

def find_note(hanzi, source_deck):
    """Find note by Hanzi in source deck, then broader search."""
    card_id = generate_card_id(hanzi)

    # 1. Try by Card_Number first (most reliable)
    for query in [
        f'"Card_Number:{card_id}"',
        f'"deck:{source_deck}" "Hanzi:{hanzi}"',
        f'"Hanzi:{hanzi}"',
    ]:
        try:
            ids = anki_request("findNotes", query=query)
            if ids:
                notes = anki_request("notesInfo", notes=ids)
                if notes:
                    return notes[0]
        except Exception:
            continue
    return None


# ============================================================
# Detect note type
# ============================================================

def detect_note_type(source_deck):
    try:
        ids = anki_request("findNotes", query=f'"deck:{source_deck}"')
        if ids:
            notes = anki_request("notesInfo", notes=ids[:1])
            if notes:
                return notes[0]["modelName"]
    except Exception:
        pass
    return None


# ============================================================
# Process one .md file (upsert: update if exists, create if new)
# ============================================================

def process_file(filepath, target_deck, source_deck):
    fname = Path(filepath).name
    print(f"\n{'='*40}")
    print(f"  File: {fname}")

    data = parse_md(filepath)
    meta = data["meta"]
    hanzi = meta.get("Hanzi", "")

    if not hanzi:
        print(f"  [ERR] Khong tim thay Hanzi trong META")
        return False

    card_id = generate_card_id(hanzi)
    print(f"  Hanzi: {hanzi}  Card_Number: {card_id}")

    # Build all fields from .md
    all_fields = build_fields(data)

    # Find existing note
    print(f"  Tim note trong Anki...")
    existing = find_note(hanzi, source_deck)

    if existing:
        note_id = existing["noteId"]
        model = existing["modelName"]
        print(f"  [OK] Tim thay note #{note_id} ({model})")

        # Filter to only valid fields for this note type
        valid_fields = set(existing["fields"].keys())
        update_fields = {k: v for k, v in all_fields.items() if k in valid_fields}

        # Don't overwrite audio/image fields (keep from old deck)
        keep_fields = {"Word_Audio", "Sentence_Audio", "Sentence_Image"}
        for kf in keep_fields:
            if kf in update_fields:
                old_val = existing["fields"].get(kf, {}).get("value", "")
                if old_val:  # Old deck has data -> keep it
                    del update_fields[kf]

        # Don't overwrite Sentence_ZH/EN if old deck has them and .md doesn't
        for sf in ["Sentence_ZH", "Sentence_EN"]:
            if sf not in all_fields and sf in valid_fields:
                pass  # keep old value
            elif sf in update_fields:
                old_val = existing["fields"].get(sf, {}).get("value", "")
                if old_val and sf not in data["meta"]:
                    del update_fields[sf]

        if update_fields:
            anki_request("updateNoteFields", note={"id": note_id, "fields": update_fields})
            print(f"  [OK] Da cap nhat {len(update_fields)} fields:")
            for k in sorted(update_fields.keys()):
                v = update_fields[k]
                short = (v[:40] + "...") if len(v) > 40 else v
                print(f"        {k}: {short}")

        # Move to target deck
        anki_request("createDeck", deck=target_deck)
        cards = anki_request("findCards", query=f"nid:{note_id}")
        if cards:
            anki_request("changeDeck", cards=cards, deck=target_deck)
            print(f"  [OK] Da chuyen -> {target_deck}")

        return True
    else:
        print(f"  [WARN] Khong co trong deck cu -> Tao note moi")

        model_name = detect_note_type(source_deck)
        if not model_name:
            print(f"  [ERR] Khong detect duoc note type")
            return False

        # Filter valid fields
        model_fields = anki_request("modelFieldNames", modelName=model_name)
        if model_fields:
            all_fields = {k: v for k, v in all_fields.items() if k in model_fields}

        anki_request("createDeck", deck=target_deck)
        tags = [f"HSK{meta.get('HSK', '')}"]

        try:
            result = anki_request("addNote", note={
                "deckName": target_deck,
                "modelName": model_name,
                "fields": all_fields,
                "tags": tags,
            })
            print(f"  [OK] Tao note moi #{result}")
            return True
        except Exception as e:
            print(f"  [ERR] {e}")
            return False


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Sync Chinese vocab .md -> Anki")
    parser.add_argument("--day", required=True, help='Ten ngay: "Day 1"')
    parser.add_argument("--input-dir", default="./output", help="Thu muc .md")
    parser.add_argument("--words", help="Danh sach Hanzi, ngan boi dau phay")
    parser.add_argument("--source-deck", default=SOURCE_DECK, help="Deck nguon")
    parser.add_argument("--target-prefix", default=TARGET_DECK_PREFIX, help="Prefix deck dich")

    args = parser.parse_args()
    source_deck = args.source_deck
    target_deck = f"{args.target_prefix}::{args.day}"
    input_dir = Path(args.input_dir)

    print("Anki Chinese Vocab Sync")
    print(f"  Source : {source_deck}")
    print(f"  Target : {target_deck}")
    print(f"  Input  : {input_dir}")

    ver = anki_request("version")
    print(f"  AnkiConnect: v{ver}")

    # Find .md files
    if args.words:
        word_list = [w.strip() for w in args.words.split(",")]
        md_files = []
        for f in input_dir.glob("*.md"):
            d = parse_md(f)
            if d["meta"].get("Hanzi") in word_list:
                md_files.append(f)
        found = {parse_md(f)["meta"].get("Hanzi") for f in md_files}
        missing = set(word_list) - found
        if missing:
            print(f"  [WARN] Chua co file .md cho: {', '.join(missing)}")
    else:
        md_files = sorted(input_dir.glob("*.md"))

    if not md_files:
        print("[WARN] Khong tim thay file .md nao.")
        sys.exit(1)

    print(f"  Tim thay {len(md_files)} file(s)")

    ok = 0
    for f in md_files:
        if process_file(f, target_deck, source_deck):
            ok += 1

    print(f"\n{'='*40}")
    print(f"  Hoan tat: {ok}/{len(md_files)} thanh cong")
    print(f"  Deck: {target_deck}")


if __name__ == "__main__":
    main()
