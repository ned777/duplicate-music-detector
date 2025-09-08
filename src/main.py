from pathlib import Path
from itertools import combinations

folder_path = input ("Drag the specific music folder that you want to scan into this window.")

# Remove extra quotes if they exist
folder_path = folder_path.strip('"')

folder=Path(folder_path)

music_list = [file for file in folder.iterdir() if file.suffix.lower() in {".mp3", ".wav", ".flac"}]
print(music_list)


# define what "same" means: filename without extension, lowercase
def key(p: Path) -> str:
    return p.stem.lower().strip()

# compare every file against every other file
for a, b in combinations(music_list, 2):
    if key(a) == key(b):
        print("dup:", a.name, "<->", b.name) 