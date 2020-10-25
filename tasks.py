from os import environ
from pathlib import Path
from invoke import task


def get_venv():
    """Return virtual environment path or throw an error if not found"""
    env = environ.get("VIRTUAL_ENV", None)
    if env:
        return Path(env)
    else:
        raise EnvironmentError("No virtual environment found.")


PKG_NAME = "data-files"
PKG_PATH = Path(f"pelican/plugins/{PKG_NAME}")
VENV_PATH = get_venv()
VENV = str(VENV_PATH.expanduser())


@task
def flake8(c):
    """Run flake8 linter with config specified in setup.cfg"""
    c.run(f"{VENV}/bin/flake8 {PKG_PATH} tasks.py setup.py")


@task
def black(c, check=False, diff=False):
    """Run black formatter in check or diff mode"""
    CF, DF = "", ""
    if check:
        CF = "--check"
    if diff:
        DF = "--diff"

    c.run(f"{VENV}/bin/black {CF} {DF} {PKG_PATH} tasks.py setup.py")


@task
def lint(c):
    """Run all linting tools"""
    black(c, check=True)
    flake8(c)
