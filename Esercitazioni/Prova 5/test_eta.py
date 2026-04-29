import pytest
from eta import controlla_eta


def test_controlla_eta():
    with pytest.raises(ValueError, match= "L'età non può essere negativa!"):
        assert controlla_eta(-1)