"""Console script for {{cookiecutter.project_slug}}."""
from __future__ import annotations

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse

{%- endif %}
{%- if cookiecutter.command_line_interface|lower != 'typer' %}
import sys

{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click

{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'typer' %}
import typer


app = typer.Typer()

@app.command()
def main() -> int:
    """Console script for {{cookiecutter.project_slug}}.

    Returns
    -------
    int
        Returncode
    """
    typer.echo("Replace this message by putting your code into {{cookiecutter.project_slug}}.cli.main")
    typer.echo("See click documentation at https://typer.tiangolo.com/")
    return 0
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None) -> int:
    """Console script for {{cookiecutter.project_slug}}.

    Parameters
    ----------
    args : list, optional
        Commandlineargs, by default None

    Returns
    -------
    int
        Returncode
    """
    click.echo("Replace this message by putting your code into {{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main() -> int:
    """Console script for {{cookiecutter.project_slug}}.

    Returns
    -------
    int
        Returncode
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into {{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
    app()
{% else %}
    sys.exit(main())  # pragma: no cover
{%- endif %}
