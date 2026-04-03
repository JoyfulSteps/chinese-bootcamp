"""Quick test: parse .md files and print fields (no Anki needed)."""
import sys
sys.path.insert(0, ".")
from scripts.anki_sync import parse_md, build_fields, generate_card_id

for name in ["output/我_wo.md", "output/你_ni.md"]:
    try:
        data = parse_md(name)
        fields = build_fields(data)
        print(f"\n{'='*50}")
        print(f"File: {name}")
        print(f"{'='*50}")
        for k, v in fields.items():
            short = (v[:60] + "...") if len(v) > 60 else v
            short = short.replace("\n", " ")
            print(f"  {k:20s} = {short}")
    except Exception as e:
        print(f"ERROR: {name} -> {e}")
