def valida_temperatura(gradi: int) -> str:
    if gradi < -273:
        raise ValueError("Temperatura sotto lo zero assoluto. Impossibile.")
    return "Lettura termica valida."