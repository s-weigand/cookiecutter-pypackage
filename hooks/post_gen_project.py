#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def run_pre_commit():
    """Init git repository, install and run pre-commit."""
    print("Initializing git repository and running precommit on all files.")
    subprocess.run("git init", cwd=PROJECT_DIRECTORY)
    subprocess.run("git add .", cwd=PROJECT_DIRECTORY)
    subprocess.run("pre-commit install", cwd=PROJECT_DIRECTORY)
    subprocess.run("pre-commit run --all", cwd=PROJECT_DIRECTORY)


if __name__ == "__main__":

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)
    if "{{cookiecutter.install_pre_commit}}" == "yes":
        run_pre_commit()
