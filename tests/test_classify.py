import pytest

from riskband import classify_band


def test_boundaries():
    assert classify_band(4, 4) == "A"
    assert classify_band(5, 3) == "B"
    assert classify_band(3, 3) == "C"
    assert classify_band(2, 2) == "D"


def test_invalid_input():
    with pytest.raises(ValueError):
        classify_band(0, 4)
