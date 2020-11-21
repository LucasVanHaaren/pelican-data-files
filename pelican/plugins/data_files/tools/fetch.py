import argparse
import os
import shutil
import sys


# directory where data files are stored in a theme
DATA_DIR = "data"


def err(msg, die=None):
    """Print an error message and exits if an exit code is given"""
    sys.stderr.write(f"ERROR: {msg}\n")
    if die:
        sys.exit(die if type(die) is int else 1)


try:
    import pelican
except ImportError:
    err(
        "Cannot import pelican.\nYou must "
        "install Pelican in order to run this script.",
        -1,
    )


def _parse_args():
    parser = argparse.ArgumentParser(
        description="""Fetch data files from compatible themes"""
    )

    parser.add_argument(
        "theme",
        type=str,
        metavar="THEME_NAME",
        help="the theme to fetch data files",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite files already present in your project",
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="show verbose output"
    )

    return parser.parse_args()


def _get_theme_path():
    return os.path.join(os.path.dirname(os.path.abspath(pelican.__file__)), "themes")


def _get_themes():
    theme_path = _get_theme_path()
    for i in os.listdir(theme_path):
        e = os.path.join(theme_path, i)
        if os.path.isdir(e):
            if os.path.islink(e):
                yield (e, os.readlink(e))
            else:
                yield (e, None)


def _print_themes(v=False):
    themes = _get_themes()
    for t, l in themes:
        if not v:
            t = os.path.basename(t)
        if l:
            if v:
                print(t + (" (symbolic link to `" + l + "')"))
            else:
                print(t + "@")
        else:
            print(t)


def main():
    """Main function, called by entrypoint"""
    args = _parse_args()

    for t in _get_themes():
        if args.theme == os.path.basename(t[0]):
            print(f"{args.theme} theme found.")
            path = os.path.join(t[0], DATA_DIR)
            if os.path.exists(path):
                print(f"{args.theme} data/ directory found.")
                dest_path = os.path.join(".", DATA_DIR)
                try:
                    if args.force:
                        shutil.rmtree(dest_path)
                    shutil.copytree(path, dest_path)
                except FileExistsError:
                    err(f"data/ dir already exists in your project.", die=2)
                print(f"{args.theme} data/ directory copied to project root folder.")
            else:
                err(f"{args.theme} data/ directory not found.")
            sys.exit(0)

    err(f"{args.theme} is not a valid theme.", die=2)
