🎮 Reaction Arena Game

A fast-paced reaction-time browser game built with Python + Flask, fully tested with pytest, linted with ruff, and managed using uv.
The project also includes a live deployment on Railway, allowing anyone to play the game online.

✨ Features

🔥 Fast reaction-time game (HTML + JavaScript frontend)

🧠 Python backend for score evaluation

🧪 Fully tested with pytest

🧹 Clean codebase using ruff

⚡ Dependency & environment management with uv

☁️ Live deployment on Railway (*.up.railway.app)

📡 JSON API (/api/score, /health)

🧩 Modular structure (logic isolated for easy testing)

📁 Project Structure
reaction-arena-game/
│
├─ reaction_game/
│   ├─ __init__.py
│   ├─ app.py               → Flask backend (UI + API)
│   ├─ logic.py             → Score evaluation logic
│   └─ templates/
│         └─ index.html     → Reaction game UI
│
├─ tests/
│   ├─ test_app.py          → API tests
│   └─ test_logic.py        → Logic tests
│
├─ pyproject.toml           → uv project configuration
├─ ruff.toml                → ruff linting rules
├─ requirements.txt         → Required packages for Railway
└─ README.md

🚀 Installation
This project uses uv as the Python package manager.
1. Install uv
pip install uv
Verify:
uv --version

📦 Install Dependencies
Inside the project folder:
uv sync
This installs:
Flask
pytest
ruff

▶️ Running the Game (Local Development)
To launch the game backend locally:
uv run python -m reaction_game.app
If successful, you will see:
Running on http://127.0.0.1:5000

🕹 Play the Game

Open in your browser:

http://127.0.0.1:5000/

Health Check
http://127.0.0.1:5000/health


Returns:

{"status": "ok"}

🎯 Game Rules

Game duration: 20 seconds

Click the red circle as fast as possible

Circle shrinks as score increases (difficulty increases)

Fast combo hits (within 700ms) increase score multiplier (up to x5)

Clicking empty space: −1 point penalty

Score is sent to backend (/api/score) and evaluated

Performance Levels (logic.py)
Score	Rating
0–5	poor
6–15	average
16–25	good
26+	excellent
🧪 Running Tests

Run all test suites:

uv run pytest


Expected output:

2 passed in X.XXs

🧹 Linting with ruff

Check code quality:

uv run ruff check .


Auto-fix issues:

uv run ruff check . --fix

🌍 Live Demo (Railway Deployment)

This project is deployed on Railway.
You can play the game online here:

👉 LIVE DEMO:
https://reaction-arena-game-production.up.railway.app


☁️ Deployment Guide (Railway)
1. Project Requirements

Railway needs:

Python 3.11+

requirements.txt (Railway installs dependencies from this file)

A Start Command

2. Start Command (Railway → Settings)
python -m reaction_game.app

3. Ensure your app binds to the correct host & port

In app.py:

port = int(os.getenv("PORT", "5000"))
app.run(debug=False, host="0.0.0.0", port=port)

4. Generate a Public Domain

Railway → Service → Settings → Public Networking / Generate Domain

A public link like this will appear:

https://reaction-arena-game.up.railway.app

📡 API Endpoints
GET /health

Returns server status:

{"status": "ok"}

POST /api/score

Submit score:

{ "score": 17 }


Response:

{
  "score": 17,
  "performance": "good"
}

👨‍🏫 Instructor Notes (Technical Requirements Coverage)
Requirement	Status
Python code quality	✔ ruff, modular structure
uv	✔ project managed with uv
ruff	✔ linting included
pytest	✔ unit tests included
Frontend UI	✔ index.html
Deployment	✔ Railway live demo
API Design	✔ REST endpoints
