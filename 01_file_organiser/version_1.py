from __future__ import annotations

import argparse
import shutil
from pathlib import Path


CATEGORY_MAP = {
    "PDFs": {".pdf"},
    "Videos": {
        ".mp4",
        ".mkv",
        ".mov",
        ".avi",
        ".wmv",
        ".flv",
        ".webm",
        ".mpeg",
        ".mpg",
        ".m4v",
    },
    "Images": {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp",
        ".svg",
        ".tiff",
        ".ico",
        ".heic",
    },
}


def get_category(file_path: Path) -> str:
    extension = file_path.suffix.lower()

    for category, extensions in CATEGORY_MAP.items():
        if extension in extensions:
            return category

    return "Others"


def build_unique_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        candidate = destination.with_name(new_name)
        if not candidate.exists():
            return candidate
        counter += 1


def organize_folder(
    folder_path: Path, skip_files: set[Path] | None = None
) -> dict[str, int]:
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder_path}")

    if not folder_path.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder_path}")

    skip_files = {path.resolve() for path in (skip_files or set())}
    summary = {"PDFs": 0, "Videos": 0, "Images": 0, "Others": 0}

    for item in folder_path.iterdir():
        if not item.is_file():
            continue
        if item.resolve() in skip_files:
            continue

        category = get_category(item)
        destination_folder = folder_path / category
        destination_folder.mkdir(exist_ok=True)

        destination = build_unique_destination(destination_folder / item.name)
        shutil.move(str(item), str(destination))
        summary[category] += 1

    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organize a folder into PDFs, Videos, Images, and Others."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=Path.home() / "Downloads",
        type=Path,
        help="Folder to organize. Defaults to your Downloads folder.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_folder = args.folder.expanduser().resolve()
    script_path = Path(__file__).resolve()
    summary = organize_folder(target_folder, skip_files={script_path})

    print(f"Organized folder: {target_folder}")
    print(f"PDFs moved: {summary['PDFs']}")
    print(f"Videos moved: {summary['Videos']}")
    print(f"Images moved: {summary['Images']}")
    print(f"Other files moved: {summary['Others']}")


if __name__ == "__main__":
    main()
