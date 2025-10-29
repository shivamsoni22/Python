from docx import Document
import re
import pandas as pd
import os

def extract_tags_from_docx(filepath):
    """
    Function to extract JSON-like tags from a Word document.
    Tags are assumed to be in format: "tag_name":
    """
    doc = Document(filepath)
    text = "\n".join([p.text for p in doc.paragraphs])
    tags = re.findall(r'"([a-zA-Z0-9_]+)"\s*:', text)
    return set(tags)

# -----------------------
# Step 1: File paths
# -----------------------
file_live = r"C:\Users\shivam.soni\Desktop\R&D\R&D\josnToFindTag\live.docx"
file_seller = r"C:\Users\shivam.soni\Desktop\R&D\R&D\josnToFindTag\Brand catalog example (2).docx"

# -----------------------
# Step 2: Extract tags
# -----------------------
tags_live = extract_tags_from_docx(file_live)
tags_seller = extract_tags_from_docx(file_seller)

# -----------------------
# Step 3: Combine unique tags
# -----------------------
all_tags = sorted(tags_live.union(tags_seller))

# -----------------------
# Step 4: Build comparison table
# -----------------------
data = []
for tag in all_tags:
    in_live = tag in tags_live
    in_seller = tag in tags_seller
    in_both = in_live and in_seller
    data.append([tag, in_both, in_live, in_seller])

# -----------------------
# Step 5: Ensure output folder exists
# -----------------------
output_dir = r"C:\Users\shivam.soni\Desktop\R&D\R&D\josnToFindTag"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "Brand_catalog.xlsx")

# -----------------------
# Step 6: Export to Excel
# -----------------------
df = pd.DataFrame(data, columns=[
    "Tag Name",
    "Present_in_Both",
    "Present_in_live",
    "Present_in_Brand_catalog"
])
df.to_excel(output_path, index=False)

print(f"✅ Comparison Excel saved at: {output_path}")




