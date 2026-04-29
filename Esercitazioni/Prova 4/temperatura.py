def leggi_umidita():
    return 50


def allarme_pioggia() -> str:
    umidita = leggi_umidita()
    if umidita > 90 and umidita < 99:
        return "Allarme: Pioggia imminente!"
    if umidita > 100:
        return "Allarme: CATASTROFE CLIMATICA"
    return "Cielo sereno."