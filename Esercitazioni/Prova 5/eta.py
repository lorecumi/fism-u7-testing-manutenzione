# main.py

def controlla_eta(eta):
    if eta < 0:
        # Lanciamo l'errore perché l'età non può essere negativa
        raise ValueError("L'età non può essere negativa!")
    return f"Hai {eta} anni."