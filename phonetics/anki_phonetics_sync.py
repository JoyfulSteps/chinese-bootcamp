"""
Pinyin Phonetics → Anki Sync
Parse phonetics .md files -> create Note Type -> sync via AnkiConnect.

Usage:
    python phonetics/anki_phonetics_sync.py                        # Sync all
    python phonetics/anki_phonetics_sync.py --sounds "e,ü,zh"     # Sync specific sounds
    python phonetics/anki_phonetics_sync.py --create-model-only    # Only create the note type
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
DECK_NAME = "Chinese Foundation::Phonetics"
MODEL_NAME = "Pinyin Phonetics"
CLIPS_DIR = Path(__file__).parent / "clips"
OUTPUT_DIR = Path(__file__).parent / "output"

FIELDS = [
    "Pinyin",           # e, ü, zh...
    "IPA",              # /ɤ/, /y/, /ʈʂ/...
    "Type",             # Vận mẫu đơn, Thanh mẫu...
    "Category",         # Nguyên âm đơn (单韵母)
    "Difficulty",       # ⭐⭐, ⭐⭐⭐
    "Compare_With",     # u, "e" tiếng Việt
    "Teacher_Note",     # Quote from teacher
    "Video_Clip",       # [sound:xxx.mp4]
    "Not_This",         # HTML
    "Actually_Is",      # HTML
    "Practice_Steps",   # HTML
    "Confusion_Pair",   # HTML
    "Spelling_Rules",   # HTML
    "Sample_Words",     # HTML
    "Mnemonic",         # text
    "Common_Errors",    # HTML
]


def anki_request(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params})
    req = urllib.request.Request(ANKI_URL, data=payload.encode("utf-8"))
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"[ERR] Cannot connect to Anki: {e}")
        sys.exit(1)
    if result.get("error"):
        raise Exception(result["error"])
    return result.get("result")


# ══════════════════════════════════
# Create Note Type
# ══════════════════════════════════

def read_template(filename):
    """Read HTML template file."""
    template_dir = Path(__file__).parent / "anki_card"
    filepath = template_dir / filename
    if filepath.exists():
        return filepath.read_text(encoding="utf-8")
    return ""


def create_model():
    """Create the Pinyin Phonetics note type in Anki."""
    # Check if model exists
    existing = anki_request("modelNames")
    if MODEL_NAME in existing:
        print(f"  [OK] Note type '{MODEL_NAME}' already exists")
        return True

    front_html = read_template("front.html")
    back_html = read_template("back.html")
    css = read_template("style.css")

    if not front_html or not back_html:
        print("  [ERR] Template files not found in anki_card/")
        return False

    anki_request("createModel",
        modelName=MODEL_NAME,
        inOrderFields=FIELDS,
        cardTemplates=[{
            "Name": "Phonetics Card",
            "Front": front_html,
            "Back": back_html,
        }],
        css=css,
    )
    print(f"  [OK] Created note type: {MODEL_NAME}")
    return True


# ══════════════════════════════════
# Parse .md file
# ══════════════════════════════════

def parse_phonetics_md(filepath):
    """Parse a phonetics .md file into field dict."""
    text = Path(filepath).read_text(encoding="utf-8")

    result = {}
    sections = {
        "NOT_THIS": "Not_This",
        "ACTUALLY_IS": "Actually_Is",
        "PRACTICE_STEPS": "Practice_Steps",
        "CONFUSION_PAIR": "Confusion_Pair",
        "SPELLING_RULES": "Spelling_Rules",
        "SAMPLE_WORDS": "Sample_Words",
        "MNEMONIC": "Mnemonic",
        "COMMON_ERRORS": "Common_Errors",
        "META": "_meta",
    }

    # Split by ---SECTION_NAME---
    parts = re.split(r'---(\w+)---', text)

    i = 1
    while i < len(parts) - 1:
        key = parts[i].strip()
        val = parts[i + 1].strip()
        field_name = sections.get(key)
        if field_name:
            result[field_name] = val
        i += 2

    # Parse META
    meta = {}
    if "_meta" in result:
        for line in result.pop("_meta").split("\n"):
            line = line.strip()
            if ": " in line:
                k, v = line.split(": ", 1)
                meta[k.strip()] = v.strip()

    # Map meta to fields
    result["Pinyin"] = meta.get("Pinyin", "")
    result["IPA"] = meta.get("IPA", "")
    result["Type"] = meta.get("Type", "")
    result["Category"] = meta.get("Category", "")
    result["Difficulty"] = meta.get("Difficulty", "")
    result["Compare_With"] = meta.get("Compare_With", "")
    result["Teacher_Note"] = meta.get("Teacher_Note", "")

    # Video clip
    video_file = meta.get("Video_File", "")
    if video_file:
        result["Video_Clip"] = f"[sound:{video_file}]"
    else:
        result["Video_Clip"] = ""

    return result


# ══════════════════════════════════
# Store video clips to Anki media
# ══════════════════════════════════

def store_media(video_filename):
    """Copy video clip to Anki media folder."""
    clip_path = CLIPS_DIR / video_filename
    if not clip_path.exists():
        print(f"  [WARN] Clip not found: {clip_path}")
        return False

    import base64
    data = clip_path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")

    anki_request("storeMediaFile",
        filename=video_filename,
        data=b64,
    )
    size_kb = len(data) / 1024
    print(f"  [OK] Stored media: {video_filename} ({size_kb:.0f}KB)")
    return True


# ══════════════════════════════════
# Upsert note
# ══════════════════════════════════

def find_note(pinyin):
    """Find existing note by Pinyin field."""
    query = f'"deck:{DECK_NAME}" "Pinyin:{pinyin}"'
    try:
        ids = anki_request("findNotes", query=query)
        if ids:
            notes = anki_request("notesInfo", notes=ids)
            if notes:
                return notes[0]
    except Exception:
        pass

    # Broader search
    query = f'"Pinyin:{pinyin}" "note:{MODEL_NAME}"'
    try:
        ids = anki_request("findNotes", query=query)
        if ids:
            notes = anki_request("notesInfo", notes=ids)
            if notes:
                return notes[0]
    except Exception:
        pass
    return None


def process_file(filepath):
    """Process one .md file → upsert into Anki."""
    fname = Path(filepath).name
    print(f"\n{'=' * 40}")
    print(f"  File: {fname}")

    fields = parse_phonetics_md(filepath)
    pinyin = fields.get("Pinyin", "")

    if not pinyin:
        print(f"  [ERR] No Pinyin found in META")
        return False

    print(f"  Pinyin: {pinyin}  Type: {fields.get('Type', '')}")

    # Store video clip
    video_file = fields.get("Video_Clip", "")
    if video_file:
        actual_filename = video_file.replace("[sound:", "").replace("]", "")
        if actual_filename:
            store_media(actual_filename)

    # Find existing note
    existing = find_note(pinyin)

    if existing:
        note_id = existing["noteId"]
        print(f"  [OK] Found existing note #{note_id} → updating")

        valid_fields = set(existing["fields"].keys())
        update_fields = {k: v for k, v in fields.items() if k in valid_fields}

        anki_request("updateNoteFields", note={"id": note_id, "fields": update_fields})
        print(f"  [OK] Updated {len(update_fields)} fields")
        return True
    else:
        print(f"  [NEW] Creating new note...")

        # Create deck
        anki_request("createDeck", deck=DECK_NAME)

        # Ensure all fields exist
        for f in FIELDS:
            if f not in fields:
                fields[f] = ""

        try:
            result = anki_request("addNote", note={
                "deckName": DECK_NAME,
                "modelName": MODEL_NAME,
                "fields": fields,
                "tags": [
                    f"phonetics",
                    f"type::{fields.get('Type', '').replace(' ', '_')}",
                ],
            })
            print(f"  [OK] Created note #{result}")
            return True
        except Exception as e:
            print(f"  [ERR] {e}")
            return False


# ══════════════════════════════════
# Main
# ══════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Sync Pinyin Phonetics → Anki")
    parser.add_argument("--sounds", help="Comma-separated sounds to sync (default: all)")
    parser.add_argument("--input-dir", default=str(OUTPUT_DIR), help="Directory with .md files")
    parser.add_argument("--create-model-only", action="store_true", help="Only create note type")
    args = parser.parse_args()

    print("=" * 50)
    print("  Pinyin Phonetics → Anki Sync")
    print("=" * 50)

    # Check Anki connection
    ver = anki_request("version")
    print(f"  AnkiConnect: v{ver}")
    print(f"  Deck: {DECK_NAME}")
    print(f"  Model: {MODEL_NAME}")

    # Create note type
    if not create_model():
        sys.exit(1)

    if args.create_model_only:
        print("\n  Done (model only mode)")
        return

    # Find .md files
    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        print(f"  [ERR] Directory not found: {input_dir}")
        sys.exit(1)

    sounds_filter = None
    if args.sounds:
        sounds_filter = set(s.strip().lower() for s in args.sounds.split(","))

    md_files = sorted(input_dir.glob("*.md"))
    if sounds_filter:
        md_files = [f for f in md_files if f.stem.lower() in sounds_filter]

    if not md_files:
        print("  [WARN] No .md files found")
        sys.exit(1)

    print(f"  Found {len(md_files)} file(s)")

    # Process files
    ok = 0
    for f in md_files:
        if process_file(f):
            ok += 1

    print(f"\n{'=' * 50}")
    print(f"  Done! {ok}/{len(md_files)} synced successfully")
    print(f"  Deck: {DECK_NAME}")


if __name__ == "__main__":
    main()
