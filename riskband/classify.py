"""PSRB band classification helpers.

The standard defines four bands (A-D) over a product score computed from two
1-5 ordinal ratings:

    score = likelihood * severity

Band cut-offs (normative):
    A: 16 <= score <= 25
    B: 10 <= score <= 15
    C:  5 <= score <=  9
    D:  1 <= score <=  4
"""

from __future__ import annotations

BAND_THRESHOLDS = {
    "A": (16, 25),
    "B": (10, 15),
    "C": (5, 9),
    "D": (1, 4),
}

BAND_LABELS = {
    "A": "Band A - Critical",
    "B": "Band B - Advanced",
    "C": "Band C - Elevated",
    "D": "Band D - Baseline",
}


def classify_band(likelihood: int, severity: int) -> str:
    """Map a likelihood/severity pair (both 1-5) to a PSRB band."""
    if not (1 <= int(likelihood) <= 5 and 1 <= int(severity) <= 5):
        raise ValueError("likelihood and severity must be integers in 1..5")
    score = int(likelihood) * int(severity)
    for band, (low, high) in BAND_THRESHOLDS.items():
        if low <= score <= high:
            return band
    raise ValueError(f"score {score} is outside the PSRB range")
