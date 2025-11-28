from __future__ import annotations

import os
from flask import Flask, jsonify, render_template, request

from .logic import evaluate_score

app = Flask(__name__)


@app.get("/")
def index():
    """Render the game UI."""
    return render_template("index.html")


@app.get("/health")
def healthcheck():
    """Simple health check endpoint."""
    return jsonify({"status": "ok"}), 200


@app.post("/api/score")
def score_endpoint():
    """
    Receive a score and return its performance level.
    """
    data = request.get_json(force=True)
    score = int(data.get("score", 0))

    result = evaluate_score(score)
    return jsonify({"score": score, "performance": result}), 200


# -----------------------------------------------------
# ✔ Single correct run block (Works on Railway & local)
# -----------------------------------------------------
if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))   # Railway provides PORT automatically
    app.run(debug=False, host="0.0.0.0", port=port)
