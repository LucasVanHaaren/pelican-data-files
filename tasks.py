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


@task
def clean(c, dist=False, build=False):
    """Clean build directories"""
    patterns = []
    if dist:
        patterns.append("dist/")
    if build:
        patterns.append("build/")

    for p in patterns:
        c.run(f"rm -rf {p}")


@task()
def build(c, source=False, wheel=False, egg=False):
    """Build source and wheel package"""
    SF, WF, EF = "", "", ""
    if source:
        SF = "sdist"
    if wheel:
        WF = "bdist_wheel"
    if egg:
        WF = "bdist_egg"
    if source or wheel or egg:
        clean(c, dist=True, build=True)
        return c.run(f"python setup.py {SF} {WF} {EF}", hide=True, warn=True)


@task
def buildcheck(c):
    """Check if builds are OK"""
    return c.run("twine check dist/*")


@task
def publish(c, prod=False):
    """Publish package on PyPI"""
    build_res = build(c, source=True, wheel=True)
    if build_res.ok:
        build_check_res = buildcheck(c)
        if build_check_res.ok:
            if prod:
                c.run("twine upload dist/*")
            else:
                c.run("twine upload -r testpypi dist/*")
