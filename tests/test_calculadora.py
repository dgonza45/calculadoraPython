import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_cuadrado_positivo(self):
        self.assertEqual(self.calc.cuadrado(5.0), 25.0)

    def test_cuadrado_cero(self):
        self.assertEqual(self.calc.cuadrado(0.0), 0.0)

    def test_cuadrado_negativo(self):
        self.assertEqual(self.calc.cuadrado(-4.0), 16.0)

    def test_cubo_positivo(self):
        self.assertEqual(self.calc.cubo(5.0), 125.0)

    def test_cubo_negativo(self):
        self.assertEqual(self.calc.cubo(-4.0), -64.0)

if __name__ == '__main__':
    unittest.main()
