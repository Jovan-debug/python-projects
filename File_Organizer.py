import shutil
from pathlib import Path


class FileOrganizer:
    # Dictionary mapping category names to allowed extensions
    CATEGORIES = {
        "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
        "Documents": {".pdf", ".docx", ".txt", ".xlsx", ".csv"},
        "Media": {".mp3", ".mp4", ".mkv", ".wav", ".avi"},
        "Archives": {".zip", ".tar", ".gz", ".7z", ".rar"},
    }

    def __init__(self, folder_path: Path):
        self.source_dir = Path(folder_path)

    def organize(self):
        moved_count = 0
        try:
            for item in self.source_dir.iterdir():
                # Process only files (ignore directories like the category folders themselves)
                if not item.is_file():
                    continue

                ext = item.suffix.lower()

                # Find which category matches the file extension
                for category, extensions in self.CATEGORIES.items():
                    if ext in extensions:
                        category_folder = self.source_dir / category
                        category_folder.mkdir(parents=True, exist_ok=True)  # Create folder only when needed

                        destination = category_folder / item.name
                        shutil.move(item, destination)
                        moved_count += 1
                        break  # Stop checking other categories once matched

            print(f"✅ File organization complete! Successfully moved {moved_count} file(s).")

        except PermissionError:
            print("❌ Error: Permission denied. A file might be currently open or locked.")
        except Exception as e:
            print(f"❌ Unexpected error during organization: {e}")


def get_path(prompt: str) -> Path:
    while True:
        raw_path = input(prompt).strip()
        path_to_check = Path(raw_path)
        if path_to_check.exists() and path_to_check.is_dir():
            return path_to_check
        print("Invalid path! Please enter an existing folder path.")


def main():
    print("***** Welcome to the File Organizer Program *****")
    folder_path = get_path("Enter the folder path to organize: ")
    organizer = FileOrganizer(folder_path=folder_path)
    organizer.organize()


if __name__ == "__main__":
    main()