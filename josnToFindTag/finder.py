from docx import Document
import re
import pandas as pd
from collections import Counter

# Step 1: Load Word file
doc = Document(r"C:\Users\shivam.soni\Desktop\R&D\R&D\josnToFindTag\seller catalog (2).docx")

# Step 2: Extract all text from document
full_text = ""
for para in doc.paragraphs:
    full_text += para.text + "\n"

# Step 3: Clean text
json_text = full_text.strip()

# Step 4: Find all JSON-like keys (pattern for "key":)
pattern = r'"([a-zA-Z0-9_]+)"\s*:'
keys = re.findall(pattern, json_text)

# Step 5: Count frequency of each key
key_counts = Counter(keys)

# Step 6: Create a DataFrame for Excel
df = pd.DataFrame(list(key_counts.items()), columns=["Tag Name", "Count"])
df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)

# Step 7: Save to Excel file
output_path = r"C:\Users\shivam.soni\Desktop\R&D\R&D\josnToFindTag\unique_tags.xlsx"
df.to_excel(output_path, index=False, sheet_name="Tags")

print("✅ Excel file successfully created!")
print(f"📁 Saved at: {output_path}")
print(f"Total unique tags found: {len(df)}")
