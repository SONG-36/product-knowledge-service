import os
import json
from pathlib import Path
from split_params import split_parameters

OCR_DIR = "output/ocr_raw"
OUT_FILE = "output/structured/structured.json"

os.makedirs("output/structured", exist_ok=True)

all_blocks = []

for fname in sorted(os.listdir(OCR_DIR)):
    if not fname.endswith(".txt"):
        continue

    text = Path(os.path.join(OCR_DIR, fname)).read_text(encoding="utf-8")

    params = split_parameters(text)

    for p in params:
        all_blocks.append({
            "source_file": fname,
            "field": p["field"],
            "value": p["value"]
        })

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_blocks, f, ensure_ascii=False, indent=2)

print(f"Generated {len(all_blocks)} parameter blocks")
