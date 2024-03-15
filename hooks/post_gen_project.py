#!/usr/bin/env python
from __future__ import annotations

import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path().cwd()


def run_pre_commit():
    """Init git repository, install and run pre-commit."""
    print("Initializing git repository and running pre-commit on all files.")
    subprocess.run(
        "git config --global init.defaultBranch main", cwd=PROJECT_DIRECTORY, shell=True
    )
    subprocess.run("git init", cwd=PROJECT_DIRECTORY, shell=True)
    subprocess.run("git add .", cwd=PROJECT_DIRECTORY, shell=True)
    subprocess.run("pre-commit install", cwd=PROJECT_DIRECTORY, shell=True)
    subprocess.run("pre-commit run --all", cwd=PROJECT_DIRECTORY, shell=True, check=False)


if __name__ == "__main__":
    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        (PROJECT_DIRECTORY / "{{ cookiecutter.project_slug }}" / "cli.py").unlink(missing_ok=True)
        (PROJECT_DIRECTORY / "tests" / "test_cli.py").unlink(missing_ok=True)
    else:
        (PROJECT_DIRECTORY / "tests" / "test_dummy.py").unlink(missing_ok=True)
    if "{{cookiecutter.install_pre_commit}}" == "yes":
        run_pre_commit()
