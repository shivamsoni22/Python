import pandas as pd
import json
import os

# ------------------ CONFIGURATION ------------------
INPUT_FILE = r"C:\Users\shivam.soni\Desktop\R&D\R&D\new\statues.xlsx"
OUTPUT_FILE = r"C:\Users\shivam.soni\Desktop\R&D\R&D\new\pipeS\statues.xlsx"
# ---------------------------------------------------

def is_json(value):
    """Check if a string is valid JSON."""
    if not isinstance(value, str):
        return False
    value = value.strip()
    if not (value.startswith('{') or value.startswith('[')):
        return False
    try:
        json.loads(value)
        return True
    except:
        return False


def flatten_json_to_string(json_str):
    """Flatten nested JSON and return as a | separated string with last key only."""
    try:
        obj = json.loads(json_str)
    except:
        return json_str  # not JSON, return original

    flat_items = []

    def recurse(inner_obj):
        if isinstance(inner_obj, dict):
            for k, v in inner_obj.items():
                if isinstance(v, (dict, list)):
                    recurse(v)
                else:
                    v = str(v).strip() if v not in [None, ""] else "N/A"
                    flat_items.append(f"{k}: {v}")
        elif isinstance(inner_obj, list):
            for item in inner_obj:
                if isinstance(item, (dict, list)):
                    recurse(item)
                else:
                    item = str(item).strip() if item not in [None, ""] else "N/A"
                    flat_items.append(str(item))
        else:
            inner_obj = str(inner_obj).strip() if inner_obj not in [None, ""] else "N/A"
            flat_items.append(str(inner_obj))

    recurse(obj)
    return " | ".join(flat_items)


# ------------------ MAIN EXECUTION ------------------

print("📘 Input file loaded successfully.")
df = pd.read_excel(INPUT_FILE)

# Fill NaN with N/A
df = df.fillna("N/A")

# Detect JSON columns using sampling (rechecking logic)
json_columns = []
for col in df.columns:
    sample_values = df[col].astype(str).head(10)
    if any(is_json(v) for v in sample_values):
        json_columns.append(col)

print(f"🔍 Detected JSON columns: {json_columns}")

# Remove old file if exists
try:
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
except PermissionError:
    print("⚠️ Output file open hai, please close and rerun.")
    exit()

# Process JSON columns
for col in json_columns:
    print(f"🚀 Flattening JSON column → {col}")
    df[col] = df[col].astype(str).apply(lambda x: flatten_json_to_string(x) if is_json(x) else x)

# Replace blanks with N/A (final cleaning)
df = df.replace("", "N/A")

# Save to Excel
df.to_excel(OUTPUT_FILE, index=False)
print(f"✅ Output saved successfully at: {OUTPUT_FILE}")
