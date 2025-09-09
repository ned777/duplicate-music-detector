from pathlib import Path
import eyed3
import warnings
import logging

# Suppress DeprecationWarnings from Python
warnings.filterwarnings("ignore", category=DeprecationWarning)
# Silence eyeD3 log spam
eyed3.log.setLevel(logging.ERROR)

folder_path = input("Drag the specific music folder that you want to scan into this window: ").strip('"')
folder = Path(folder_path)

title_map = {}  # title -> list of filenames

for file in folder.iterdir():
    if file.suffix.lower() == ".mp3":
        audio = eyed3.load(str(file))
        if audio and audio.tag:
            title = audio.tag.title if audio.tag.title else file.stem
        else:
            title = file.stem

        # Normalize titles (ignore case & spaces)
        norm_title = title.strip().lower()
        title_map.setdefault(norm_title, []).append(file.name)

# Print duplicates with filenames
found_duplicates = False
for title, files in title_map.items():
    if len(files) > 1:
        found_duplicates = True
        print(f"\nDuplicate title: {title}")
        for f in files:
            print(f"  - {f}")

if not found_duplicates:
    print("No duplicate titles found.")
