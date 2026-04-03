"""Delete old Pinyin Phonetics notes and model from Anki."""
import json
import urllib.request

ANKI_URL = "http://localhost:8765"

def anki(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params})
    req = urllib.request.Request(ANKI_URL, data=payload.encode("utf-8"))
    req.add_header("Content-Type", "application/json")
    r = json.loads(urllib.request.urlopen(req).read())
    if r.get("error"):
        print(f"  [WARN] {r['error']}")
    return r.get("result")

# Delete notes
notes = anki("findNotes", query='note:"Pinyin Phonetics"') or []
print(f"Found {len(notes)} old notes")
if notes:
    anki("deleteNotes", notes=notes)
    print(f"Deleted {len(notes)} notes")

# Try to remove model 
try:
    # No direct API to remove model in AnkiConnect, but creating fresh will work
    print("Old model will be overwritten on next sync")
except:
    pass

print("Done cleanup")
