"""
Test per le funzioni matematiche di base.
"""
import unittest
from mathutils.basic import somma, sottrazione, moltiplicazione, divisione

class TestBasicFunctions(unittest.TestCase):
    
    def test_somma(self):
        self.assertEqual(somma(2, 3), 5)
        self.assertEqual(somma(-1, 1), 0)
        self.assertEqual(somma(0, 0), 0)
        
    def test_sottrazione(self):
        self.assertEqual(sottrazione(5, 3), 2)
        self.assertEqual(sottrazione(3, 5), -2)
        self.assertEqual(sottrazione(0, 0), 0)
        
    def test_moltiplicazione(self):
        self.assertEqual(moltiplicazione(2, 3), 6)
        self.assertEqual(moltiplicazione(-2, 3), -6)
        self.assertEqual(moltiplicazione(0, 5), 0)
        
    def test_divisione(self):
        self.assertEqual(divisione(6, 3), 2)
        self.assertEqual(divisione(5, 2), 2.5)
        self.assertEqual(divisione(0, 5), 0)
        
    def test_divisione_per_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divisione(5, 0)
            
if __name__ == '__main__':
    unittest.main()
