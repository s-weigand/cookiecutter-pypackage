#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner

{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
import re

from typer.testing import CliRunner

{%- endif %}


{%- if cookiecutter.command_line_interface|lower in ['click', "typer"] %}
from {{cookiecutter.project_slug}} import cli

{%- endif %}


{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_slug }}.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.app)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_slug }}.cli.main" in result.output
    help_result = runner.invoke(cli.app, ["--help"])
    assert help_result.exit_code == 0
    assert re.search(r"--help\s+Show this message and exit.", help_result.output)
{%- endif %}
