# {{ cookiecutter.project_name }}

[![PyPi Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug_url }}/)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/{{ cookiecutter.project_slug_url }}.svg)](https://anaconda.org/conda-forge/{{ cookiecutter.project_slug_url }})
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug_url }}/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

{% if 'https://github.com' == cookiecutter.git_host_url %}
[![Actions Status]({{ cookiecutter.git_host_url}}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_url }}/workflows/Tests/badge.svg)]({{ cookiecutter.git_host_url}}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_url }}/actions)
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug_url }}/badge/?version=latest)](https://{{ cookiecutter.project_slug_url }}.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_url }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_url }})
[![Documentation Coverage](https://raw.githubusercontent.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_url }}/main/docs/\_static/interrogate_badge.svg)]({{ cookiecutter.git_host_url}}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_url }})

[![All Contributors](https://img.shields.io/github/all-contributors/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_url }})](#contributors)
{% endif %}
[![Code style Python: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

{{ cookiecutter.project_short_description }}

- Free software: {{ cookiecutter.open_source_license }}
- Documentation: https://{{ cookiecutter.project_slug_url }}.readthedocs.io.

## Features

- TODO
