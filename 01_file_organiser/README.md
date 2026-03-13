# File Organiser

This script organizes the files in one folder into 4 folders:

- `PDFs`
- `Videos`
- `Images`
- `Others`

## How to use it

### Step 1

Copy `version_1.py` into the folder you want to organize.

Example:

If you want to organize your Downloads folder, put `version_1.py` inside your Downloads folder.

### Step 2

Open the terminal in that exact folder.

Example for Downloads:

```powershell
cd "C:\Users\Arun Yadav\Downloads"
```

### Step 3

Run this command:

```powershell
py .\version_1.py
```

## What happens after running

The script will create these folders inside the same folder:

- `PDFs`
- `Videos`
- `Images`
- `Others`

Then it will move:

- all PDF files into `PDFs`
- all video files into `Videos`
- all image files into `Images`
- all remaining files into `Others`

## Example

If your folder has:

- `resume.pdf`
- `movie.mp4`
- `photo.jpg`
- `notes.txt`

After running the script, it will become:

- `PDFs\resume.pdf`
- `Videos\movie.mp4`
- `Images\photo.jpg`
- `Others\notes.txt`
