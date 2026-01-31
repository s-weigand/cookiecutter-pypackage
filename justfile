# Cruft/Cookiecutter template development workflow
# Use 'just --list' to see all available recipes

# Set shell for Windows compatibility
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

BAKE_OPTIONS := "--no-input"

# Default recipe (show available recipes)
default:
    @just --list

# Generate project using defaults
bake:
    uv run cruft create {{BAKE_OPTIONS}} . --overwrite-if-exists

# Generate project using defaults and watch for changes
watch: bake
    uv run watchfiles --ignore-paths python_boilerplate 'just bake' .

# Check if project is up to date with template
check:
    uv run cruft check

# Update existing project to latest template version
update:
    uv run cruft update

# Show diff between project and template
diff:
    uv run cruft diff

# Re-create project using existing .cruft.json and watch for changes
replay: watch
