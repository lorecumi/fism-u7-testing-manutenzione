import pytest
from temperature import valida_temperatura

def test_valida_temperatura():
    assert valida_temperatura(20) == "Lettura termica valida."

def test_zero_assoluto():
    with pytest.raises(ValueError):
        valida_temperatura(-274)
