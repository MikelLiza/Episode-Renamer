# 📺 TV Show Episode Renamer

A Python script that automatically renames TV show episode files using metadata from [TVmaze API](https://www.tvmaze.com/api). Perfect for organizing your media collection with proper episode titles.

Example: (Before) avatar_s01e01.mp4 ---> (After) 1-1 The Boy in the Iceberg.mp4
## Features ✨
- **Automatic Metadata Fetching**: Retrieves episode titles from TVmaze API
- **Season Folder Support**: Processes all season folders in your directory
- **Smart Filename Sanitization**: Removes illegal characters from filenames
- **Flexible Matching**: Supports year-based show identification
- **Preserves File Extensions**: Keeps original file formats (mp4, mkv, etc.)

## Installation ⚙️

### Prerequisites
- Python 3.6+
- `requests` library

### Setup
1. Install the required package:
   ```bash
   pip install requests

    Download the script:
    bash
    Copy

    wget https://raw.githubusercontent.com/your-username/mikelliza-episode-renamer/main/tvmaze_renamer.py

Usage 🚀
Basic Command
bash
Copy

python tvmaze_renamer.py

Configuration

Edit these variables at the bottom of the script:
python
Copy

show_name = "Your Show Name"  # Required
show_year = "2020"           # Optional (helps disambiguate shows)
base_folder = "path/to/your/show"  # Path containing Season folders

Expected Folder Structure
Copy

Your_Show_Name/
├── Season 1/
│   ├── episode1.mp4
│   ├── episode2.mkv
│   └── ...
├── Season 2/
│   ├── episode1.avi
│   └── ...
└── ...

Output Format

Files will be renamed to:
{season}-{episode} {sanitized_title}.{ext}
Example: 1-3 The Southern Air Temple.mp4
How It Works 🔍

    Queries TVmaze API to find your show's ID

    Fetches all episode titles for the show

    Processes each Season folder:

        Matches files to episodes in order

        Sanitizes titles (removes illegal chars)

        Renames files while preserving extensions

Example 📝

Before:
Copy

Season 1/
├── avatar_s01e01.mp4
├── avatar_s01e02.mkv
└── ...

After:
Copy

Season 1/
├── 1-1 The Boy in the Iceberg.mp4
├── 1-2 The Avatar Returns.mkv
└── ...

Future Improvements 💡

    Add command-line arguments

    Support multiple shows in one run

    Add dry-run mode

    Implement episode number validation

    Add progress bars

License 📄

MIT License - Free to use and modify

Note: Always back up your files before running bulk rename operations!
