# File Organizer Script

## Project Overview

The File Organizer Script is a Python automation project that
organizes files into separate folders based on their file extensions.

It helps keep directories clean and makes files easier to find.

## Features

- Automatically organizes files by extension.
- Creates destination folders when required.
- Prevents overwriting files with duplicate names.
- Supports dry-run mode to preview changes.
- Logs successful file movements.
- Handles invalid folder paths.
- Supports Windows and other platforms with Python installed.

## Technologies Used

- Python 3
- pathlib
- shutil
- argparse
- logging

## Project Structure

    File-Organizer-Script/
    ├── main.py
    ├── README.md
    ├── file_organizer.log
    └── test_files/
        ├── docx/
        ├── jpg/
        ├── pdf/
        ├── py/
        └── txt/

## Requirements

- Python 3.10 or later
- Visual Studio Code (optional)

No third-party Python packages are required.

## How to Run

### 1. Clone the repository

    git clone YOUR_GITHUB_REPOSITORY_URL

### 2. Open the project folder

    cd YOUR_PROJECT_FOLDER

### 3. Preview file organization

    python main.py --dry-run

### 4. Organize files

    python main.py

### 5. Organize a specific folder

    python main.py "C:\path\to\your\folder"

## Dry-Run Mode

Dry-run mode displays the planned file movements without
actually moving any files.

Example:

    python main.py --dry-run

## Logging

The script records successful file movements in
file_organizer.log.

## Future Improvements

- Schedule automatic file organization.
- Add support for custom file categories.
- Improve error reporting.
- Add automated tests.

## Learning Outcomes

- Python scripting and automation.
- File and directory management.
- Exception handling.
- Logging.
- Command-line arguments.
- Safe file operations.

## Author

Rayyan