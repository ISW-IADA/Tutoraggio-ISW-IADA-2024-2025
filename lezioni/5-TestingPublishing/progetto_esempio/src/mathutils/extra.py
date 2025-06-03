"""
Esempio per dimostrare il calcolo della coverage dei test.

Eseguire con:
coverage run -m pytest
coverage report
coverage html
"""

def fibonacci(n):
    """Calcola l'n-esimo numero della sequenza di Fibonacci."""
    if n < 0:
        raise ValueError("L'indice non può essere negativo")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def is_prime(n):
    """Verifica se un numero è primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Questa funzione non sarà coperta dai test
def calcola_fattoriale(n):
    """Calcola il fattoriale di n."""
    if n < 0:
        raise ValueError("L'indice non può essere negativo")
    if n == 0 or n == 1:
        return 1
    return n * calcola_fattoriale(n-1)
