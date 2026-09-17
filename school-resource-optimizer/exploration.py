import os
import pandas as pd

os.makedirs("data", exist_ok=True)

url = "https://www.men.gov.ma/sites/default/files/statistique_2024-25%20VF%20(2)_1.xlsx"
local_backup = "data/backup_statistiques.xlsx"

# try downloading live; if it fails (no internet, link changed...), use the local backup file
try:
    print(f"Reading Data from : {url}")
    raw = pd.read_excel(url, sheet_name="Stat 2024-2025", header=None)
except Exception as e:
    print(f"Live download failed ({e}), using local backup instead")
    raw = pd.read_excel(local_backup, sheet_name="Stat 2024-2025", header=None)

# this Excel file is not a clean table: it's a printed report with titles and
# blank rows mixed in. The numbers we need are always on fixed row positions,
# so we grab them directly using .iloc[row, column]

# Public schools: row 17 = students, 18 = classes, 19 = rooms, 20 = establishments
# columns: 2 = Primaire, 3 = Collegial, 4 = Qualifiant
public_students = raw.iloc[17, 2:5].tolist()
public_classes = raw.iloc[18, 2:5].tolist()
public_rooms = raw.iloc[19, 2:5].tolist()
public_establishments = raw.iloc[20, 2:5].tolist()

# Private schools: row 42 = students, 43 = classes, 44 = rooms (no establishments row)
private_students = raw.iloc[42, 2:5].tolist()
private_classes = raw.iloc[43, 2:5].tolist()
private_rooms = raw.iloc[44, 2:5].tolist()

levels = ["Primaire", "Collegial", "Qualifiant"]

rows = []

category_id = 1
for i in range(3):
    rows.append({
        "category_id": category_id,
        "level": levels[i],
        "sector": "Public",
        "students": int(public_students[i]),
        "classes": int(public_classes[i]),
        "rooms": int(public_rooms[i]),
        "establishments": int(public_establishments[i]),
    })
    category_id += 1

for i in range(3):
    rows.append({
        "category_id": category_id,
        "level": levels[i],
        "sector": "Prive",
        "students": int(private_students[i]),
        "classes": int(private_classes[i]),
        "rooms": int(private_rooms[i]),
        "establishments": 0,  # not available for private schools in this report
    })
    category_id += 1

df_cleaned = pd.DataFrame(rows)

output_path = "data/processed_schools.csv"
df_cleaned.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"Done! Clean dataset saved to {output_path}")
print(df_cleaned)
