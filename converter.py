import os, sys, subprocess, argparse
from pathlib import Path

class Converter:
    def __init__(self):
        pass

    def arg_parser(self):
        parser = argparse.ArgumentParser(description="Convert .cue files to .chd files")
        parser.add_argument("--folder", required=True, help="Folder to scan for .cue files")
        parser.add_argument("--recursive", action="store_true", help="Scan subfolders")
        parser.add_argument("--force",action="store_true", help="Overwrite existing .chd files")
        parser.add_argument("--dry-run", action="store_true", help="Show commands only")
        args = parser.parse_args()

    def scan_folder(self, root: Path, recursive: bool):
        root = Path(root)
        if not root.exists() or not root.is_dir():
            raise ValueError(f"Not a valid folder: {root}")


if __name__ == "__main__":
    converter = Converter()
    converter.arg_parser()
    print("Folder: ", args.folder)
    print("Recursive: ", args.recursive)
    print("Force: ", args.force)
    print("Dry Run: ", args.dry_run)

