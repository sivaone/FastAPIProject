# FastAPIProject

This repository contains a small FastAPI project and a VS Code Dev Container configuration to run and develop it locally in Docker.

## What the devcontainer does

- Uses the official Python devcontainer image.
- Installs the recommended VS Code extensions (Python, Pylance, Docker).
- Forwards port `8000` from the container to the host.
- Runs `python -m pip install --upgrade pip && python -m pip install -r requirements.txt` after the container is created.

## Prerequisites

- Docker (Docker Engine) installed and running on your machine.
- Visual Studio Code with the "Dev Containers" (a.k.a. Remote - Containers) extension installed.
- (Optional) `code` CLI if you want to open VS Code from the terminal.

## Open the project in a Dev Container (VS Code)

1. Open this repository in VS Code.
2. Open the Command Palette (F1 or Ctrl+Shift+P) and choose:

   "Dev Containers: Reopen in Container"

   VS Code will build or pull the devcontainer image and open the workspace inside the container. The `postCreateCommand` in `.devcontainer/devcontainer.json` will run and install dependencies from `requirements.txt`.

3. To rebuild the container after changing `.devcontainer/*`, use the Command Palette and choose:

   "Dev Containers: Rebuild Container"

## Run the FastAPI app inside the container

Open a terminal in VS Code (the terminal will be inside the container). Then run:

```bash
# (optional) ensure dependencies are installed
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# run the app (assumes `main.py` defines `app`)
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000 in your browser. The interactive API docs are available at http://localhost:8000/docs.

## Run locally without the Dev Container

If you prefer to run the project on your host machine instead of in the container:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Troubleshooting

- If the container build fails, make sure Docker is running and you have enough disk space.
- If dependencies didn't install, open a terminal inside the container and run `python -m pip install -r requirements.txt` manually to see the error.
- If port 8000 is not reachable, confirm the port is forwarded in `.devcontainer/devcontainer.json` and that no local process is blocking the port.
- Use `docker ps` and `docker logs <container-id>` to inspect the running container and logs.

## (Optional) Access the running container

If you need to run commands inside the container you can open a terminal in VS Code (Terminal → New Terminal) after the devcontainer starts, or use `docker exec` from the host. Keep in mind changes you make interactively are ephemeral unless persisted in the Dockerfile or a volume.

### Install code-server manually (optional)

If you want a browser-accessible VS Code instance inside the running devcontainer, you can install and run code-server manually from a terminal opened inside the container. This is useful for quick, ad-hoc browser access and avoids changing the Dockerfile.

Run these commands inside the devcontainer terminal:

```bash
# install code-server (official installer)
curl -fsSL https://code-server.dev/install.sh | sh

# set a strong password for this session (do not commit this)
export PASSWORD="your-strong-password"

# start code-server in the background, serving the workspace on port 8080
nohup code-server --auth password --bind-addr 0.0.0.0:8080 /workspace/${localWorkspaceFolderBasename} > /tmp/code-server.log 2>&1 &

# on the host, open http://localhost:8080 in your browser
```

Notes and security

- Port forwarding: if VS Code doesn't expose port 8080 automatically, add 8080 to the `forwardPorts` array in `.devcontainer/devcontainer.json` or use the Ports view in VS Code to forward it.
- Ephemeral: installing and running code-server this way is ephemeral — the install and any config will be lost if you rebuild or recreate the container. Add the install to the Dockerfile or use `postCreateCommand` to persist.
- Security: never expose port 8080 publicly without TLS and a strong password. For remote access prefer a reverse proxy with TLS or an SSH tunnel.

## Next steps / optional improvements

- Add a custom `Dockerfile` in `.devcontainer/` if you need system packages.
- Add a `devcontainer.json` variant that uses Docker Compose if you need dependent services (Redis, Postgres, etc.).
- Add a VS Code `launch.json` and a `tasks.json` to automate running and debugging the app.

---

If you want, I can add a `launch.json` for attaching the debugger to uvicorn, or add a `Dockerfile` variant—tell me which you'd prefer.
