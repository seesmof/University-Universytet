import os

POTOCHNA_TEKA: str = os.path.dirname(os.path.abspath(__file__))
STO_MEGABAJT = 100 * 1024 * 1024

fajly = set([".obsidian", "__pycache__", ".venv"])
potribna_teka = os.path.join(POTOCHNA_TEKA, "../")
for root, dirs, files in os.walk(potribna_teka):
    for file in files:
        file_size = os.path.getsize(os.path.join(root, file))
        if file_size >= STO_MEGABAJT:
            fajly.add(file)
            print(f"Znajshlo fajl {file}")

with open(os.path.join(potribna_teka, ".gitignore"), "w", encoding="utf-8") as f:
    for fajl in fajly:
        f.write(f"{fajl}\n")
