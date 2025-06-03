"""
Funzioni matematiche di base.
"""

def somma(a, b):
    """Calcola la somma di due numeri."""
    return a + b

def sottrazione(a, b):
    """Calcola la differenza tra due numeri."""
    return a - b

def moltiplicazione(a, b):
    """Calcola il prodotto di due numeri."""
    return a * b

def divisione(a, b):
    """
    Calcola il quoziente di due numeri.
    
    Args:
        a: numeratore
        b: denominatore
    
    Returns:
        float: risultato della divisione
    
    Raises:
        ZeroDivisionError: se il denominatore è zero
    """
    if b == 0:
        raise ZeroDivisionError("Impossibile dividere per zero")
    return a / b
