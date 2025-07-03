import unittest
from Calculadora.Calculadora import Calculadora

class CalculadoraTeste(unittest.TestCase):
    def testeSoma(self):
        calculadora = Calculadora()
        resultado = calculadora.soma(2, 3)

        self.assertEqual(5, resultado)

if __name__ == '__main__':
    unittest.main()

# tearDown
#setUp