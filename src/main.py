from pathlib import Path

folder_path = input ("Drag the specific music folder that you want to scan into this window.")

# Remove extra quotes if they exist
folder_path = folder_path.strip('"')

folder=Path(folder_path)

for file in folder.iterdir():
    if file.suffix.lower() in [".mp3", ".wav", ".flac"]:
        print(file)
