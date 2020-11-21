import argparse
import shutil
import sys
from pathlib import Path


def _err(msg, die=None):
    """Print an error message and exits if an exit code is given"""
    sys.stderr.write(f"ERROR: {msg}\n")
    if die:
        sys.exit(die if type(die) is int else 1)


try:
    import pelican
except ImportError:
    _err(
        "Cannot import pelican.\nYou must "
        "install Pelican in order to run this script.",
        1,
    )

# where data files are stored in pelican-data-files's compatible theme
SRC_DATA_DIR = "data"

# where data file are copied in pelican project directory
DEST_DATA_DIR = "data"

PELICAN_ROOT_DIR = Path(pelican.__file__).absolute().parent
PELICAN_THEMES_DIR = PELICAN_ROOT_DIR.joinpath("themes")


def _parse_args():
    """Parse and return cli arguments"""
    parser = argparse.ArgumentParser(
        description="""List and fetch data files from compatible themes"""
    )

    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="list all themes compatible with this plugin",
    )

    parser.add_argument(
        "-f",
        "--fetch",
        type=str,
        metavar="THEME_NAME",
        help="fetch theme's data files",
    )

    # parser.add_argument(
    #     "--force",
    #     action="store_true",
    #     help="overwrite files already present in your project",
    # )

    # if no args parsed, set --help
    return parser.parse_args(None if sys.argv[1:] else ["--help"])


def _get_themes():
    return [theme for theme in PELICAN_THEMES_DIR.iterdir() if theme.is_dir()]


def _get_compatible_themes(themes):
    return [theme for theme in themes if _is_compatible(theme)]


def _is_compatible(theme):
    return theme.joinpath(SRC_DATA_DIR).exists()


def _fetch_files(theme):
    try:
        shutil.copytree(
            theme.joinpath(SRC_DATA_DIR), Path.cwd().joinpath(DEST_DATA_DIR)
        )
    except FileExistsError:
        _err(
            f"Cannot copy '{theme.name}' files, "
            f"directory '{DEST_DATA_DIR}' already exists.",
            die=2,
        )
    else:
        print(f"'{theme.name}' files successfully fetched.")


def main():
    """Main function, called by entrypoint"""
    args = _parse_args()

    if args.list:
        for theme in _get_compatible_themes(_get_themes()):
            print(f"{theme.name}")
        sys.exit(0)

    if args.fetch:
        theme = PELICAN_THEMES_DIR.joinpath(args.fetch)
        if theme.exists():
            if _is_compatible(theme):
                _fetch_files(theme)
                sys.exit(0)
            else:
                _err(f"'{args.fetch}' is not a compatible theme.", die=2)
        else:
            _err(f"'{args.fetch}' is not an existing theme.", die=2)
