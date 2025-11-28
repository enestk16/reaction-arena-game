from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from .logic import evaluate_score

app = Flask(__name__)


@app.get("/")
def index():
    """Oyun arayüzünü döndürür."""
    return render_template("index.html")


@app.get("/health")
def healthcheck():
    """Basit bir health check endpointi."""
    return jsonify({"status": "ok"}), 200


@app.post("/api/score")
def score_endpoint():
    """
    Oyuncu skoru gönderir.
    Backend skoru işler ve performans seviyesi döndürür.
    """
    data = request.get_json(force=True)
    score = int(data.get("score", 0))

    result = evaluate_score(score)
    return jsonify({"score": score, "performance": result}), 200


if __name__ == "__main__":
    app.run(debug=True)
