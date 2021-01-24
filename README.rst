======================
Cookiecutter PyPackage
======================

My opinionated fork of https://github.com/audreyr/cookiecutter-pypackage/

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/s-weigand/cookiecutter-pypackage


Trouble-shooting
----------------

If you have an older git version (e.g. git-bash for windows) that doesn't know about ``main`` as default branch name and you get::

    fatal: invalid branch name: init.defaultBranch =

you can globally set the default branch name to ``main``, by running::

    git config --global init.defaultBranch main
