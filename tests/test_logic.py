from __future__ import annotations

from reaction_game.logic import evaluate_score


def test_score_levels():
    assert evaluate_score(2) == "poor"
    assert evaluate_score(10) == "average"
    assert evaluate_score(20) == "good"
    assert evaluate_score(40) == "excellent"
