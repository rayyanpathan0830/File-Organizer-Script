
import os
import shutil
import logging
import argparse
from pathlib import Path

# Folder where this Python script is located
BASE_DIR = Path(__file__).resolve().parent

# Save logs in a separate file
LOG_FILE = BASE_DIR / "file_organizer.log"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def get_unique_path(destination):
    """Avoid overwriting a file with the same name."""
    if not destination.exists():
        return destination

    folder = destination.parent
    stem = destination.stem
    suffix = destination.suffix
    counter = 1

    while True:
        new_path = folder / f"{stem}_{counter}{suffix}"
        if not new_path.exists():
            return new_path
        counter += 1

def organize_files(folder_path, dry_run=False):
    """Organize files into folders based on file extensions."""
    folder = Path(folder_path).resolve()

    if not folder.exists() or not folder.is_dir():
        print(f"Error: Folder does not exist: {folder}")
        return

    # Snapshot files before creating destination folders
    files = [
        item for item in folder.iterdir()
        if item.is_file()
    ]

    if not files:
        print("No files found to organize.")
        return

    moved_count = 0

    for file_path in files:
        # Avoid organizing the script's own log
        if file_path.resolve() == LOG_FILE.resolve():
            continue

        # Use extension as the category
        extension = file_path.suffix.lower().lstrip(".")
        category = extension if extension else "no_extension"

        destination_folder = folder / category
        destination = destination_folder / file_path.name

        # Handle duplicate filenames
        destination = get_unique_path(destination)

        if dry_run:
            print(f"[DRY RUN] {file_path.name} -> "
                  f"{category}/{destination.name}")
            continue

        try:
            destination_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(destination))

            message = f"Moved {file_path} -> {destination}"
            logging.info(message)
            print(message)

            moved_count += 1

        except OSError as error:
            logging.exception("Failed to move %s", file_path)
            print(f"Error moving {file_path.name}: {error}")

    if dry_run:
        print("\nDry run complete. No files were moved.")
    else:
        print(f"\nOrganization complete. Files moved: {moved_count}")
        print(f"Log saved to: {LOG_FILE}")

def main():
    parser = argparse.ArgumentParser(
        description="Organize files by extension."
    )

    parser.add_argument(
        "folder",
        nargs="?",
        default=str(BASE_DIR / "test_files"),
        help="Folder to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()
    organize_files(args.folder, args.dry_run)

if __name__ == "__main__":
    main()