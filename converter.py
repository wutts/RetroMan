import pathlib, subprocess, argparse, os, sys
from installer import install_chdman, check_chdman

class Converter:
    def __init__(self):
        args = self.parse_args()

        folder = Path(args.folder)
        if not folder.is_dir():
            print(f"Error: {folder} is not a valid folder")
            sys.exit(1)

        chdman_check = check_chdman()
        if not chdman_check:
            install_chdman()
        
        cues = find_cues(folder, recursive=args.recursive)
        if len(cues) == 0:
            print(f"Error: No cues found in {folder}")
            sys.exit(1)

        converted = []
        skipped = []
        failed = []

        for cue in cues:
            success, message = convert_cue_to_chd(cue, force=args.force, dry_run=args.dry_run)
            print(message)
            if success and message.startswith("OK"):
                converted.append(cue)
            elif "SKIP" in message:
                skipped.append(cue)
            elif not success:
                failed.append(cue)

        print("\nSummary:")
        print(f"  total:    {len(cues)}")
        print(f"  converted:{len(converted)}")
        print(f"  skipped:  {len(skipped)}")
        print(f"  failed:   {len(failed)}")

        if failed:
            exit(1)
        else:
            exit(0)