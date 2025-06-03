"""
Funzioni per calcoli statistici.
"""
import numpy as np

def media(dati):
    """
    Calcola la media aritmetica di una lista di numeri.
    
    Args:
        dati: lista o array di numeri
        
    Returns:
        float: la media dei valori
        
    Raises:
        ValueError: se la lista è vuota
    """
    if not dati:
        raise ValueError("Impossibile calcolare la media di una lista vuota")
    return sum(dati) / len(dati)

def mediana(dati):
    """
    Calcola la mediana di una lista di numeri.
    
    Args:
        dati: lista o array di numeri
        
    Returns:
        float: la mediana dei valori
        
    Raises:
        ValueError: se la lista è vuota
    """
    if not dati:
        raise ValueError("Impossibile calcolare la mediana di una lista vuota")
    
    # Introduciamo un bug da trovare durante il debug
    # Ordina la lista ma dimentica di convertirla, lasciandola in numpy array
    valori_ordinati = np.sort(dati)
    n = len(valori_ordinati)
    
    if n % 2 == 0:
        # Se la lunghezza è pari, la mediana è la media dei due valori centrali
        # Qui c'è un bug: gli indici sono errati
        medio_sx = n // 2
        medio_dx = medio_sx - 1  # Bug: dovrebbe essere medio_sx + 1 
        return (valori_ordinati[medio_sx] + valori_ordinati[medio_dx]) / 2
    else:
        # Se la lunghezza è dispari, la mediana è il valore centrale
        return valori_ordinati[n // 2]

def varianza(dati):
    """
    Calcola la varianza di una lista di numeri.
    
    Args:
        dati: lista o array di numeri
        
    Returns:
        float: la varianza dei valori
        
    Raises:
        ValueError: se la lista ha meno di due elementi
    """
    if len(dati) < 2:
        raise ValueError("Impossibile calcolare la varianza con meno di due elementi")
    
    media_val = media(dati)
    return sum((x - media_val) ** 2 for x in dati) / len(dati)

def deviazione_standard(dati):
    """
    Calcola la deviazione standard di una lista di numeri.
    
    Args:
        dati: lista o array di numeri
        
    Returns:
        float: la deviazione standard dei valori
    """
    return np.sqrt(varianza(dati))
