# Copilot Instructions for FastAPIProject

## Project Overview
- This is a small FastAPI service centered on weather data loaded from `weather.json`.
- The primary API app lives in `main.py` and is served as `main:app`.
- Data is loaded once at startup via FastAPI lifespan and read from the module-level `data` object.
- `books_api.py` is a separate sample app and should not be changed unless the task explicitly mentions it.

## Tech Stack
- Python 3.14
- FastAPI
- Uvicorn
- Pytest

## Dependency and Environment Rules
- Keep dependencies minimal and pinned in `requirements.txt`.
- Prefer existing packages before adding new ones.
- If a new package is required, update `requirements.txt` and explain why.

## API Conventions
- Keep route handlers simple and explicit.
- Preserve existing response shapes unless a task explicitly asks to change them.
- Prefer clear error payloads for not-found and invalid-input scenarios.
- If changing endpoint behavior, update or add tests in `test_main.py`.

## Data Handling Conventions
- Weather source of truth is `weather.json`.
- Ensure file-reading logic remains relative to `main.py` (using `Path(__file__).parent`).
- Avoid introducing mutable global state beyond the existing `data` pattern unless explicitly required.

## Testing Requirements
- Add or update pytest tests for every functional behavior change.
- Keep tests focused on endpoint behavior via `fastapi.testclient.TestClient`.
- Verify status code and response body structure/content.

## Local Commands
- Install dependencies: `pip install -r requirements.txt`
- Run API: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
- Run tests: `pytest -q`

## Container Notes
- Docker image runs the same app entrypoint (`main:app`) on port 8000.
- Keep Dockerfile changes minimal and aligned with the local workflow.

## Code Style
- Prefer straightforward Python and explicit naming over clever abstractions.
- Keep functions small and readable.
- Add concise comments only where logic is non-obvious.
- Avoid broad refactors outside the requested task.

## Change Safety
- Do not rename endpoints, files, or public JSON fields unless requested.
- Do not modify `weather.json` schema without updating all affected endpoints and tests.
- If requirements are ambiguous, choose the least disruptive implementation.
