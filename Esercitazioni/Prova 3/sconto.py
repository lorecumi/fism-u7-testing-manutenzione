
def get_prezzo_db():
    """
    Immagina che questa funzione legga un prezzo da un database 
    molto lento o complicato da configurare.
    """
    return 100  # Valore reale nel DB

def calcola_totale_con_sconto(sconto):
    """
    Questa è la funzione che vogliamo testare. 
    Dipende da get_prezzo_db().
    """
    prezzo = get_prezzo_db()
    return prezzo - sconto