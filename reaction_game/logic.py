from __future__ import annotations


def evaluate_score(score: int) -> str:
    """
    Oyuncunun performans seviyesini döndürür.

    - 0–5  → poor
    - 6–15 → average
    - 16–25 → good
    - 26+ → excellent
    """
    if score <= 5:
        return "poor"
    if score <= 15:
        return "average"
    if score <= 25:
        return "good"
    return "excellent"
