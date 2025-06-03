"""
Test per le funzioni statistiche usando pytest.
"""
import pytest
import numpy as np
from mathutils.stats import media, mediana, varianza, deviazione_standard

# Fixture per dati di test comuni
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def empty_data():
    return []

# Test per la funzione media
def test_media_calcolo_corretto(sample_data):
    assert media(sample_data) == 3.0
    
def test_media_lista_vuota(empty_data):
    with pytest.raises(ValueError):
        media(empty_data)

# Test per la funzione mediana con parametrizzazione
@pytest.mark.parametrize("data,expected", [
    ([1, 2, 3], 2),           # Lista dispari
    ([1, 2, 3, 4], 2.5),      # Lista pari
    ([5, 2, 4, 1, 3], 3),     # Lista non ordinata
])
def test_mediana_valori_diversi(data, expected):
    assert mediana(data) == expected

# Test per la funzione varianza
def test_varianza_calcolo_corretto(sample_data):
    assert varianza(sample_data) == pytest.approx(2.0)
    
def test_varianza_lista_insufficiente():
    with pytest.raises(ValueError):
        varianza([1])

# Test per la deviazione standard
def test_deviazione_standard(sample_data):
    assert deviazione_standard(sample_data) == pytest.approx(np.sqrt(2.0))
    
# Test con mock per dimostrare come simulare dipendenze esterne
def test_media_con_mock(monkeypatch):
    # Mock della funzione sum per dimostrare l'uso di monkeypatch
    monkeypatch.setattr('builtins.sum', lambda x: 20)
    
    # Con il mock, sum([1, 2, 3, 4, 5]) restituirà 20 invece di 15
    # Quindi media([1, 2, 3, 4, 5]) sarà 20/5 = 4.0
    assert media([1, 2, 3, 4, 5]) == 4.0
