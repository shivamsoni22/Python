import pandas as pd
import json
import os
from pandas import json_normalize

# -------------------- CONFIGURATION --------------------
INPUT_FILE = r"C:\Users\shivam.soni\Desktop\R&D\R&D\new\Vases..xlsx"
OUTPUT_FILE = r"C:\Users\shivam.soni\Desktop\R&D\R&D\new\Vases01..xlsx"
# --------------------------------------------------------

def is_json(value):
    """Check if a string is valid JSON."""
    if not isinstance(value, str):
        return False
    try:
        json_object = json.loads(value)
    except (ValueError, TypeError):
        return False
    return True

def deep_expand_json_column(df, col_name):
    """
    Expand a JSON column deeply with rechecking logic:
    1. Parse JSON values.
    2. Flatten using pandas.json_normalize.
    3. Recheck if any field again contains JSON (nested JSONs).
    4. Expand recursively until all JSONs are flattened.
    """
    expanded_rows = []
    for item in df[col_name]:
        if is_json(item):
            expanded_rows.append(json.loads(item))
        else:
            expanded_rows.append({})

    expanded_df = pd.json_normalize(expanded_rows, sep=".")
    expanded_df.columns = [f"{col_name}.{c}" for c in expanded_df.columns]

    # Rechecking logic: detect if any subfield is still JSON and expand again
    nested_json_cols = []
    for subcol in expanded_df.columns:
        sample_vals = expanded_df[subcol].dropna().astype(str).head(20)
        if any(is_json(v) for v in sample_vals):
            nested_json_cols.append(subcol)

    # Recursive expansion for nested JSONs
    while nested_json_cols:
        for nested_col in nested_json_cols:
            print(f"🔁 Re-expanding nested JSON column → {nested_col}")
            deeper_expanded_rows = []
            for val in expanded_df[nested_col]:
                if is_json(val):
                    deeper_expanded_rows.append(json.loads(val))
                else:
                    deeper_expanded_rows.append({})
            deeper_df = pd.json_normalize(deeper_expanded_rows, sep=".")
            deeper_df.columns = [f"{nested_col}.{sub}" for sub in deeper_df.columns]
            expanded_df = expanded_df.drop(columns=[nested_col])
            expanded_df = pd.concat([expanded_df, deeper_df], axis=1)

        # Recheck again if further nesting exists
        nested_json_cols = []
        for subcol in expanded_df.columns:
            sample_vals = expanded_df[subcol].dropna().astype(str).head(20)
            if any(is_json(v) for v in sample_vals):
                nested_json_cols.append(subcol)

    return expanded_df

# Step 1: Read Excel
df = pd.read_excel(INPUT_FILE)
print("📘 Input file loaded successfully.")

# Step 2: Identify JSON columns
json_columns = []
for col in df.columns:
    sample_values = df[col].dropna().head(20)
    if any(is_json(v) for v in sample_values):
        json_columns.append(col)

print(f"🔍 Detected JSON columns: {json_columns}")

# Step 3: Expand and save with recheck logic
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    # Save non-JSON part
    non_json_df = df.drop(columns=json_columns, errors='ignore').fillna("N/A")
    non_json_df.to_excel(writer, sheet_name="Main_Data", index=False)

    # Expand each JSON column fully
    for col in json_columns:
        print(f"🚀 Expanding JSON column → {col}")
        expanded_df = deep_expand_json_column(df, col)
        expanded_df = expanded_df.fillna("N/A")
        expanded_df.to_excel(writer, sheet_name=col[:31], index=False)

print("\n✅ All JSON columns expanded with recheck logic successfully!")
print(f"📂 Final output saved at: {OUTPUT_FILE}")
