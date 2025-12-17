import json
import re

def extract_number(value):
    match = re.search(r"(\d+(\.\d+)?)", value)
    return float(match.group(1)) if match else None


def normalize(structured_path, mapping_path, output_path):
    with open(structured_path, encoding="utf-8") as f:
        data = json.load(f)

    with open(mapping_path, encoding="utf-8") as f:
        mapping = json.load(f)

    normalized = []

    for item in data:
        field = item["field"]
        value = item["value"]

        if field not in mapping:
            continue

        rule = mapping[field]

        norm = {
            "canonical_field": rule["canonical"],
            "raw_field": field,
            "raw_value": value,
            "value": extract_number(value) if rule["type"] == "number" else value,
            "unit": rule["unit"],
            "source_file": item["source_file"]
        }

        normalized.append(norm)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(normalized, f, ensure_ascii=False, indent=2)

    print(f"Normalized {len(normalized)} items")
