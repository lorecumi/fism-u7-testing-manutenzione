from unittest.mock import patch
from temperatura import allarme_pioggia
import pytest




@pytest.mark.parametrize("umidita, errore", [
    (50, "Cielo sereno."),
    (91, "Allarme: Pioggia imminente!"),
    (110, "Allarme: CATASTROFE CLIMATICA")
])

@patch('temperatura.leggi_umidita')
def test_allarme_pioggia(mock_umidita,umidita, errore):
    mock_umidita.return_value = umidita

    risultato = allarme_pioggia()

    assert risultato == errore

    mock_umidita.assert_called_once()