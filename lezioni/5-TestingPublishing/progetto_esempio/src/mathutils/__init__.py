"""
Mathutils - Libreria di utility matematiche per scopi didattici
"""

from .basic import somma, sottrazione, moltiplicazione, divisione
from .stats import media, mediana, varianza, deviazione_standard

__all__ = [
    'somma', 'sottrazione', 'moltiplicazione', 'divisione',
    'media', 'mediana', 'varianza', 'deviazione_standard'
]

__version__ = '0.1.0'
