"""
Pinyin Phonetics → Anki Sync
Parse phonetics .md files -> create Note Type -> sync via AnkiConnect.

Usage:
    python phonetics/anki_phonetics_sync.py                        # Sync all
    python phonetics/anki_phonetics_sync.py --sounds "e,ü,zh"     # Sync specific
    python phonetics/anki_phonetics_sync.py --create-model-only    # Only create note type
"""

import sys
import json
import re
import base64
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

# Fields in the note type
FIELDS = [
    "Pinyin",               # e, ü, zh
    "IPA",                  # /ɤ/, /y/
    "Type",                 # Vận mẫu đơn, Thanh mẫu
    "Category",             # Nguyên âm đơn · 单韵母
    "Difficulty",           # ⭐⭐, ⭐⭐⭐
    "Compare_With",         # u, "e" tiếng Việt
    "Teacher_Note",         # Quote from teacher
    "Video_Clip",           # [sound:xxx.mp4]
    "Pronunciation_Guide",  # Full HTML content (md_to_html)
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


# ============================================================
# Markdown to HTML (same as anki_sync.py)
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
    in_sub_list = False
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
        raw = line  # keep original indentation for sub-list detection

        # Table
        if s.startswith("|") and s.endswith("|"):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            in_table = True
            cells = [c for c in s.split("|")[1:-1]]
            table_rows.append(cells)
            continue
        elif in_table:
            html_parts.append(flush_table())

        # Sub-list (indented with spaces/tabs + - or *)
        if re.match(r'^    [-*] ', raw) or re.match(r'^\t[-*] ', raw):
            content = inline(s[2:])
            if not in_sub_list:
                html_parts.append("<ul style='margin-left:18px'>")
                in_sub_list = True
            html_parts.append(f"<li>{content}</li>")
            continue
        elif in_sub_list:
            html_parts.append("</ul>")
            in_sub_list = False

        # List
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

        # Numbered list
        m = re.match(r'^(\d+)\.\s+(.+)$', s)
        if m:
            content = inline(m.group(2))
            html_parts.append(f"<p><b>{m.group(1)}.</b> {content}</p>")
            continue

        # Empty line
        if not s:
            continue

        # Headers → bold paragraph
        if s.startswith("#"):
            text = re.sub(r'^#+\s*', '', s)
            continue  # Skip headers in phonetics cards

        # Emoji section headers (📍, ❌, ✅, etc.)
        if re.match(r'^[🎯📍❌✅🏋🧪🔀📝⚠💡🧠👨🎙📊🔑🎭🇫🇷]', s):
            html_parts.append(f"<h4>{inline(s)}</h4>")
            continue

        # Regular paragraph
        html_parts.append(f"<p>{inline(s)}</p>")

    if in_table:
        html_parts.append(flush_table())
    if in_sub_list:
        html_parts.append("</ul>")
    if in_list:
        html_parts.append("</ul>")
    return "\n".join(html_parts)


# ============================================================
# Parse phonetics .md file
# ============================================================

def parse_one_sound(text_block):
    """Parse a single sound block (content + ---META---)."""
    parts = re.split(r'---META---', text_block, maxsplit=1)
    main_content = parts[0].strip()
    meta_text = parts[1].strip() if len(parts) > 1 else ""

    meta = {}
    for line in meta_text.split("\n"):
        line = line.strip()
        if ": " in line:
            k, v = line.split(": ", 1)
            meta[k.strip()] = v.strip()

    pronunciation_html = md_to_html(main_content)

    fields = {
        "Pinyin": meta.get("Pinyin", ""),
        "IPA": meta.get("IPA", ""),
        "Type": meta.get("Type", ""),
        "Category": meta.get("Category", ""),
        "Difficulty": meta.get("Difficulty", ""),
        "Compare_With": meta.get("Compare_With", ""),
        "Teacher_Note": meta.get("Teacher_Note", ""),
        "Pronunciation_Guide": pronunciation_html,
    }

    video_file = meta.get("Video_File", "")
    fields["Video_Clip"] = f"[sound:{video_file}]" if video_file else ""

    return fields, meta


def parse_phonetics_md(filepath):
    """Parse a .md file. Supports multi-sound files split by ===SOUND===."""
    text = Path(filepath).read_text(encoding="utf-8")

    # Check for multi-sound file
    if "===SOUND===" in text:
        blocks = [b.strip() for b in text.split("===SOUND===") if b.strip()]
        return [parse_one_sound(b) for b in blocks]
    else:
        return [parse_one_sound(text)]


# ============================================================
# Create Note Type
# ============================================================

def read_template(filename):
    template_dir = Path(__file__).parent / "anki_card"
    filepath = template_dir / filename
    if filepath.exists():
        return filepath.read_text(encoding="utf-8")
    return ""


def create_or_update_model():
    existing = anki_request("modelNames")

    front_html = read_template("front.html")
    back_html = read_template("back.html")
    css = read_template("style.css")

    if not front_html or not back_html:
        print("  [ERR] Template files not found in anki_card/")
        return False

    if MODEL_NAME in existing:
        # Ensure all required fields exist
        try:
            current_fields = anki_request("modelFieldNames", modelName=MODEL_NAME)
            for f in FIELDS:
                if f not in current_fields:
                    anki_request("modelFieldAdd", modelName=MODEL_NAME, fieldName=f, index=len(current_fields))
                    current_fields.append(f)
                    print(f"  [OK] Added field: {f}")
        except Exception as e:
            print(f"  [WARN] Field update: {e}")

        # Update templates
        try:
            anki_request("updateModelTemplates", model={
                "name": MODEL_NAME,
                "templates": {"Phonetics Card": {"Front": front_html, "Back": back_html}}
            })
        except Exception as e:
            print(f"  [WARN] Template update: {e}")

        try:
            anki_request("updateModelStyling", model={"name": MODEL_NAME, "css": css})
        except Exception as e:
            print(f"  [WARN] Style update: {e}")

        print(f"  [OK] Updated note type: {MODEL_NAME}")
        return True

    # Create new
    anki_request("createModel",
        modelName=MODEL_NAME,
        inOrderFields=FIELDS,
        cardTemplates=[{"Name": "Phonetics Card", "Front": front_html, "Back": back_html}],
        css=css,
    )
    print(f"  [OK] Created note type: {MODEL_NAME}")
    return True


# ============================================================
# Store media
# ============================================================

def store_media(video_filename):
    clip_path = CLIPS_DIR / video_filename
    if not clip_path.exists():
        print(f"  [WARN] Clip not found: {clip_path}")
        return False

    data = clip_path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")

    anki_request("storeMediaFile", filename=video_filename, data=b64)
    size_kb = len(data) / 1024
    print(f"  [OK] Stored media: {video_filename} ({size_kb:.0f}KB)")
    return True


# ============================================================
# Upsert note
# ============================================================

def find_note(pinyin):
    for query in [
        f'"Pinyin:{pinyin}" "note:{MODEL_NAME}"',
        f'"deck:{DECK_NAME}" "Pinyin:{pinyin}"',
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


def upsert_note(fields, meta):
    """Create or update a single note in Anki."""
    pinyin = fields.get("Pinyin", "")
    if not pinyin:
        print(f"  [ERR] No Pinyin in META")
        return False

    print(f"  Pinyin: {pinyin}  Type: {fields.get('Type', '')}")

    # Store video clip
    video_ref = fields.get("Video_Clip", "")
    if video_ref:
        actual_filename = video_ref.replace("[sound:", "").replace("]", "")
        if actual_filename:
            store_media(actual_filename)

    # Find existing note
    existing = find_note(pinyin)

    if existing:
        note_id = existing["noteId"]
        print(f"  [OK] Found existing #{note_id} → updating")
        valid_fields = set(existing["fields"].keys())
        update_fields = {k: v for k, v in fields.items() if k in valid_fields}
        anki_request("updateNoteFields", note={"id": note_id, "fields": update_fields})
        print(f"  [OK] Updated {len(update_fields)} fields")
        return True
    else:
        print(f"  [NEW] Creating new note...")
        anki_request("createDeck", deck=DECK_NAME)

        for f in FIELDS:
            if f not in fields:
                fields[f] = ""

        try:
            result = anki_request("addNote", note={
                "deckName": DECK_NAME,
                "modelName": MODEL_NAME,
                "fields": fields,
                "tags": ["phonetics", f"type::{meta.get('Type', '').replace(' ', '_')}"],
            })
            print(f"  [OK] Created note #{result}")
            return True
        except Exception as e:
            print(f"  [ERR] {e}")
            return False


def process_file(filepath):
    fname = Path(filepath).name
    print(f"\n{'=' * 40}")
    print(f"  File: {fname}")

    sound_list = parse_phonetics_md(filepath)
    print(f"  Contains {len(sound_list)} sound(s)")

    ok = 0
    for fields, meta in sound_list:
        if upsert_note(fields, meta):
            ok += 1
    return ok


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Sync Pinyin Phonetics → Anki")
    parser.add_argument("--sounds", help="Comma-separated sounds to sync")
    parser.add_argument("--input-dir", default=str(OUTPUT_DIR))
    parser.add_argument("--create-model-only", action="store_true")
    args = parser.parse_args()

    print("=" * 50)
    print("  Pinyin Phonetics → Anki Sync")
    print("=" * 50)

    ver = anki_request("version")
    print(f"  AnkiConnect: v{ver}")
    print(f"  Deck: {DECK_NAME}")
    print(f"  Model: {MODEL_NAME}")

    if not create_or_update_model():
        sys.exit(1)

    if args.create_model_only:
        print("\n  Done (model only)")
        return

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        print(f"  [ERR] Dir not found: {input_dir}")
        sys.exit(1)

    sounds_filter = None
    if args.sounds:
        sounds_filter = set(s.strip().lower() for s in args.sounds.split(","))

    # Only process phonetics .md files (exclude 我_wo.md, 你_ni.md etc.)
    md_files = []
    for f in sorted(input_dir.glob("*.md")):
        # Skip vocab files (they have Hanzi_ pattern like 我_wo.md)
        stem = f.stem
        if len(stem) > 1 and "_" in stem and not stem.startswith("batch"):
            continue
        md_files.append(f)

    if sounds_filter:
        md_files = [f for f in md_files if f.stem.lower() in sounds_filter]

    if not md_files:
        print("  [WARN] No phonetics .md files found")
        sys.exit(1)

    print(f"  Found {len(md_files)} phonetics file(s)")

    ok = 0
    total = 0
    for f in md_files:
        count = process_file(f)
        ok += count
        total += 1

    print(f"\n{'=' * 50}")
    print(f"  Done! {ok} notes synced from {total} files")
    print(f"  Deck: {DECK_NAME}")


if __name__ == "__main__":
    main()
