# Modern Python Environment with `uv`

What is uv?
uv is a modern Python package and project management tool developed by Astral.
Speed: Up to 10–100x faster than traditional pip in some workflows, thanks to global caching and efficient package installation.
It is designed to be extremely fast and combines multiple Python development tasks.
`uv`manage the project environment and dependencies.
Project dependencies are declared in `pyproject.toml`, locked in `uv.lock`,
and installed into the project-local `.venv` directory.

The app loads `GROQ_API_KEY` from `.env`, sends a prompt to Groq using the
OpenAI-compatible Python client, and prints the response.

## Project files

- `app.py` - application code.
- `pyproject.toml` - project metadata and dependency declarations.
- `uv.lock` - resolved dependency versions.
- `.python-version` - requested Python version (`3.14`).
- `.venv` - local virtual environment created by `uv`.
- `.env` - local API key configuration; do not commit or share this file.

The project requires Python 3.14 or newer, as specified by
`pyproject.toml`.

## Install `uv`

If `uv` is not installed, install it with:

```powershell
python -m pip install uv
```

Check that it is available:

```powershell
uv --version
```

## Set up the project

Open a terminal in this directory and synchronize the environment from the
project's dependency files:

```powershell
uv sync  #If your project already has dependencies defined in pyproject.toml:
```

`uv sync` creates or updates `.venv` and installs the dependencies described
by `pyproject.toml` and `uv.lock`.

## Command reference for a new project

The commands below show the setup sequence for a **new** project. Run
`uv init` from the directory where you want the new project folder created.
Use a project name instead of `<directory>`:
## Powershell 

```powershell
python -m pip install uv
uv --version
checkout to project directory 
uv init 
uv venv
uv add openai python-dotenv
```
### if you are using git bash terminal 
```gitbash
# 1. Install uv
python -m pip install uv

# 2. Verify uv
uv --version

# 3.initialize the project
uv init  # it will initialize the project

# 4. Create virtual environment
uv venv 

# 5. Activate virtual environment
source .venv/Scripts/activate

# 6. Install dependencies
uv add openai python-dotenv
```


```powershell
uv run app.py
```

This folder is **already** an initialized `uv` project, so do not run
`uv init` here. To set up or restore this project's environment, use
`uv sync` as shown above.


`uv run` runs the app using the project's environment. The app makes a
request to the Groq API, so it needs an internet connection and a valid API
key.

## Manage dependencies

Add a project dependency:

```powershell
uv add package-name
```

Remove a project dependency:

```powershell
uv remove package-name
```

After changing dependencies, `uv` updates the project files. Commit
`pyproject.toml` and `uv.lock` so others can recreate the same dependency
environment. Do not commit `.venv` or `.env`.

| Operation | pip (Git Bash) | uv (Git Bash) |
|---|---|---|
| Install package | `pip install openai` | `uv add openai` |
| Create environment | `python -m venv .venv` | `uv venv` |
| Activate environment | `source .venv/Scripts/activate` | `source .venv/Scripts/activate` |
| Deactivate environment | `deactivate` | `deactivate` |
| Install requirements | `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |
| Uninstall package | `pip uninstall openai` | `uv remove openai` |
| List packages | `pip list` | `uv pip list` |
| Upgrade package | `pip install --upgrade openai` | `uv pip install --upgrade openai` |
| Freeze dependencies | `pip freeze > requirements.txt` | `uv pip freeze > requirements.txt` |
| Check version | `pip --version` | `uv --version` |



Key Features of uv
- Speed: Up to 10–100x faster than traditional pip in some workflows, thanks to global caching and efficient package installation.
- All-in-One Toolchain: Manages Python versions (uv python), virtual environments (uv venv), project dependencies (uv add, uv remove, uv sync), and lockfiles (uv.lock).
- Dependency Management: Automatically manages project dependencies through pyproject.toml.
- Reproducibility: Uses uv.lock to ensure consistent dependency versions across development environments.
- Compatibility: Supports pip-compatible commands through uv pip.
