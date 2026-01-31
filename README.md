# Cookiecutter PyPackage

My opinionated fork of https://github.com/audreyr/cookiecutter-pypackage/

## Quickstart

Install the latest [cruft](https://github.com/cruft/cruft) if you haven't installed it yet

```console
uv tool install -U cruft
```

Generate a Python package project

```console
cruft create https://github.com/s-weigand/cookiecutter-pypackage
```

## Trouble-shooting

If you have an older git version (e.g. git-bash for windows) that doesn't know about `main` as default branch name and you get

```console
fatal: invalid branch name: init.defaultBranch =
```

you can globally set the default branch name to `main`, by running

```console
git config --global init.defaultBranch main
```
