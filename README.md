🎮 Reaction Game – Python + Flask + uv + ruff + pytest
This project is a simple yet fully testable reaction-time game built with Python.
It includes:
Python backend (Flask)
Game UI (HTML + JavaScript)
uv for environment & dependency management
ruff for linting
pytest for testing
The project satisfies the technical requirements of good code quality, testing, and modern Python tooling.


📁 Project Structure
reaction-arena-game/
│
├─ reaction_game/
│   ├─ __init__.py
│   ├─ app.py             → Flask backend (runs the server & UI)
│   ├─ logic.py           → Score evaluation functions
│   └─ templates/
│         └─ index.html   → Reaction game UI
│
├─ tests/
│   ├─ test_app.py        → API tests
│   └─ test_logic.py      → Unit tests for score logic
│
├─ pyproject.toml         → uv project configuration
├─ ruff.toml              → ruff linter configuration
└─ README.md


🚀 1. Installation
Check if uv is installed:
uv --version

If not installed:
pip install uv


📦 2. Install Dependencies
In the project root directory:
uv sync

This installs:
Flask
ruff
pytest


▶️ 3. Running the Game (IMPORTANT)
To start the backend server, run:
uv run python -m reaction_game.app

If successful, you will see:
 * Running on http://127.0.0.1:5000

✔ Open the game in your browser:
http://127.0.0.1:5000/


This loads the interactive reaction game UI.

✔ Health check endpoint:
http://127.0.0.1:5000/health

Returns:
{"status": "ok"}



🧪 4. Running Tests (pytest)
To run all automated tests:
uv run pytest

You should see:
2 passed in X.XXs

Tests cover:
score evaluation logic
API behavior



🧹 5. Code Quality (ruff)
Check for linting issues:
uv run ruff check .

Automatically fix issues:
uv run ruff check . --fix

🎮 6. About the Game
The game is located in:
reaction_game/templates/index.html
Features:
20-second timed round
Target appears randomly
Target shrinks as score increases (harder gameplay)
Fast hits increase COMBO multiplier (up to x5)
Clicking empty space gives −1 penalty
Score is sent to backend on round end
Backend evaluates performance using logic.py

Performance Levels:
Score Range	Level
0–5	poor
6–15	average
16–25	good
26+	excellent


🌐 7. API Example
Send a score manually:
curl -X POST http://127.0.0.1:5000/api/score \
     -H "Content-Type: application/json" \
     -d '{"score": 17}'

Response:

{
  "score": 17,
  "performance": "good"
}


🧭 8. Developer Notes
Always run the app using:
uv run python -m reaction_game.app

Do not run:
python reaction_game/app.py
→ This will break package imports.

The code is modular so that all logic is testable.

🎓 9. Requirements Compliance Summary
Requirement	Status
Python code (good quality)	✔ ruff validation
uv	                        ✔ pyproject.toml + uv sync
ruff	                      ✔ linting config
pytest                    	✔ unit tests included
User interface             	✔ HTML/JS reaction game
Backend	                    ✔ Flask server with routes
