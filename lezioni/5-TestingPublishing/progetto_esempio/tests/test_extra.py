"""
Test per le funzioni extra per dimostrare la coverage.
"""
import pytest
from mathutils.extra import fibonacci, is_prime

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(5) == 5
    
def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(-1)
        
@pytest.mark.parametrize("num,expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (9, False),
    (17, True),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected

# Manca il test per calcola_fattoriale, quindi la coverage sarà incompleta
