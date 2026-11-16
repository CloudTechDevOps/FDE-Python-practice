# Traditional Python Environment: `venv` and `pip`

This example isolates the project's Python packages in a virtual environment
created with Python's built-in `venv` module. Dependencies are installed with
`pip` and recorded in `requirements.txt`.

The app loads `GROQ_API_KEY` from `.env`, sends a prompt to Groq using the
OpenAI-compatible Python client, and prints the response.

## Project files

- `app.py` - application code.
- `requirements.txt` - pinned package versions for reproducible installs.
- `.env` - local API key configuration; do not commit or share this file.
- `Readme.md` - this guide.

## Create and activate the environment

Run these commands from this project directory.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```
### gitbash

``` bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/Scripts/activate

```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, the terminal prompt usually shows `(.venv)`.

## Install dependencies

With the environment activated, install the pinned packages:

```bash
python -m pip install -r requirements.txt
```

## Configure the API key

Add your own Groq API key to the local `.env` file:

```dotenv
GROQ_API_KEY=your_groq_api_key
```

Do not put a real key in this README or in source code. Do not commit or share
`.env`.

## Run the application

With `.venv` activated and the dependencies installed:

```bash
python app.py
```

The app makes a request to the Groq API, so it needs an internet connection
and a valid API key.

## Check the active environment

After activation, confirm that Python points to `.venv`.

### Windows PowerShell

```powershell
$env:VIRTUAL_ENV
Get-Command python
```

### Windows Command Prompt

```cmd
echo %VIRTUAL_ENV%
where python
```

### Git Bash, macOS, or Linux

```bash
echo $VIRTUAL_ENV
which python
```

`VIRTUAL_ENV` should point to this project's `.venv` directory, and the
Python executable should be inside that directory.

## Deactivate the environment

When you are finished working in the virtual environment, run:

```bash
deactivate
```

The `(.venv)` prompt indicator disappears, and the terminal returns to its
previous Python environment.

## Other useful commands

```bash
python --version
python -m pip list
python -m pip freeze
```
