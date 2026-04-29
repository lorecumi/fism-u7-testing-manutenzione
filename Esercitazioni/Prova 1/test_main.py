import pytest
from main import addizione, divisione, sottrazione, moltiplicazione

def test_addizione():
    assert addizione(2, 3) == 5
    assert addizione(-1, 1) == 0
    assert addizione(0, 0) == 0

def test_divisione():
    assert divisione(10, 2) == 5
    assert divisione(-6, 2) == -3
    assert divisione(0, 5) == 0
    with pytest.raises(ValueError):
        divisione(5, 0)

def test_sottrazione():
    assert sottrazione(5, 3) == 2
    assert sottrazione(-1, 1) == -2
    assert sottrazione(0, 0) == 0

def test_moltiplicazione():
    assert moltiplicazione(2, 3) == 6
    assert moltiplicazione(-1, 1) == -1
    assert moltiplicazione(0, 0) == 0

