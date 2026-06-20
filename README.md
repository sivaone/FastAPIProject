# FastAPIProject

This repository contains a small FastAPI project.

## Run locally

Open a terminal in VS Code and then run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
fastapi dev main.py

# Can also run app using uvicorn
# run the app (assumes `main.py` defines `app`)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000 in your browser. The interactive API docs are available at http://localhost:8000/docs.