import logger
import shuttel 
import os

# File Organizer

A Python script that automatically organizes files into categorized directories based on their file extensions.

## Features

- Automatically creates category folders (Documents, Images, Videos, Others)
- Moves files to appropriate folders based on their extensions
- Includes logging functionality to track operations
- Error handling for failed operations

## Directory Structure

The script organizes files into the following categories:

- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`
- **Others**: Any unmatched file extensions

## Configuration

- Target Directory: `C:\Users\asus\OneDrive\Pictures`
- Log File: `file_organizer.log`
- Log Format: `timestamp:level:message`

## Functions

### `create_category_folders()`
Creates necessary category folders in the target directory if they don't exist.
- Checks for existing folders
- Creates missing folders
- Logs folder creation status

### `move_and_classify_files()`
Scans the target directory and moves files to their respective category folders.
- Identifies file extensions
- Moves files to appropriate categories
- Handles unmatched files by moving them to Others
- Logs all file movements

### `main()`
Entry point of the script that:
- Initializes folder structure
- Executes file organization
- Handles any top-level exceptions

## Usage

Run the script using Python:

```bash
python file_organizer.py
```

## Logging
The script creates a log file (`file_organizer.log`) that tracks:
- Folder creation events
- File movement operations
- Errors and exceptions
- Script completion status

## Error Handling
- All major operations are wrapped in try-except blocks
- Errors are logged with detailed messages
- Script continues running even if individual operations fail
