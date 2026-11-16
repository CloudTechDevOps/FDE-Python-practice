# Python Application Without a Virtual Environment

This example runs the application with the currently selected Python
interpreter, without creating a project-specific virtual environment.

The app loads `GROQ_API_KEY` from `.env`, sends a prompt to Groq using the
OpenAI-compatible Python client, and prints the response.

## Project files

- `app.py` - application code.
- `.env` - local API key configuration; do not commit or share this file.

## Requirements

- Python installed and available as `python`.
- A Groq API key.
- The `openai` and `python-dotenv` packages installed in the Python
  environment used to run the app.

Install the packages:

```powershell
python -m pip install openai python-dotenv
```

Add your key to `.env`:

```dotenv
GROQ_API_KEY=your_groq_api_key
```

Keep the key private. Do not paste it into source code or commit `.env`.

## Run

Open a terminal in this directory and run:

```powershell
python app.py
```

Because no project virtual environment is used, the packages are installed
into whichever Python environment `python` selects. Other projects using that
same interpreter may share those packages and versions.

