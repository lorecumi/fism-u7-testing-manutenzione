from unittest.mock import patch
from sconto import calcola_totale_con_sconto

def test_calcola_totale():
    with patch('sconto.get_prezzo_db') as mock_prezzo:
        mock_prezzo.return_value = 50

        risultato = calcola_totale_con_sconto(10)

        assert risultato == 40

        mock_prezzo.assert_called_once()





