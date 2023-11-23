from __future__ import annotations
from typing import Generator
import datetime
import os
import shlex
import subprocess
from pathlib import Path
import sys
from contextlib import contextmanager

from cookiecutter.utils import rmtree
import pytest
from pytest_cookies.plugin import Result, Cookies


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs) -> Generator[Result, None, None]:
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    print("#" * 50)
    print("result.project_path: ".upper(), result.project_path)
    print("result.exeption: ".upper(), result.exception)
    print("#" * 50)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command: str, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_year_compute_in_license_file(cookies: Cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path is not None
        license_file_path = result.project_path / "LICENSE"
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read_text()


def project_info(result: Result) -> tuple[Path, str, Path]:
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    assert result.project_path is not None
    project_path = result.project_path
    project_slug = project_path.name
    project_dir = result.project_path / project_slug
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies: Cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path is not None
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.name for f in result.project_path.glob("*")]
        assert "pyproject.toml" in found_toplevel_files
        assert "python_boilerplate" in found_toplevel_files
        assert "tests" in found_toplevel_files


def test_bake_and_run_tests(cookies: Cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path is not None
        assert result.project_path.is_dir()
        assert run_inside_dir("hatch run pytest", str(result.project_path)) == 0


def test_bake_withspecialchars_and_run_tests(cookies: Cookies):
    """Ensure that a `full_name` with double quotes does not break setup.py"""
    with bake_in_temp_dir(cookies, extra_context={"full_name": 'name "quote" name'}) as result:
        assert result.project_path is not None
        assert result.project_path.is_dir()
        assert run_inside_dir("hatch run pytest", str(result.project_path)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies: Cookies):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    with bake_in_temp_dir(cookies, extra_context={"full_name": "O'connor"}) as result:
        assert result.project_path is not None
        assert result.project_path.is_dir()
        assert run_inside_dir("hatch run pytest", str(result.project_path)) == 0


def test_make_help(cookies: Cookies):
    with bake_in_temp_dir(cookies) as result:
        # The supplied Makefile does not support win32
        if sys.platform != "win32":
            output = check_output_inside_dir("make help", str(result.project_path))
            assert b"check code coverage quickly with the default Python" in output


@pytest.mark.parametrize(
    ("license_classifier", "license_text"),
    [
        ("Apache Software License", "Licensed under the Apache License, Version 2.0"),
        ("MIT License", "MIT "),
        (
            "BSD License",
            "Redistributions of source code must retain the above copyright notice, this",
        ),
        ("ISC License", "ISC License"),
        ("GNU General Public License v3", "GNU GENERAL PUBLIC LICENSE"),
    ],
)
def test_bake_selecting_license(
    cookies: Cookies,
    license_classifier: str,
    license_text: str,
):
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": license_classifier}
    ) as result:
        assert result.project_path is not None
        assert license_text in (result.project_path / "LICENSE").read_text()
        assert license_classifier in (result.project_path / "pyproject.toml").read_text()


def test_bake_with_no_console_script(cookies: Cookies):
    context = {"command_line_interface": "No command-line interface"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" not in found_project_files

    setup_path = project_path / "pyproject.toml"
    with open(setup_path, "r") as setup_file:
        assert "[project.scripts]" not in setup_file.read()


@pytest.mark.parametrize("cli_framework_name", ("typer", "Click", "Argparse"))
def test_bake_with_console_script_files(cookies: Cookies, cli_framework_name: str):
    context = {"command_line_interface": cli_framework_name}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" in found_project_files

    setup_path = project_path / "pyproject.toml"
    with open(setup_path, "r") as setup_file:
        assert "[project.scripts]" in setup_file.read()
