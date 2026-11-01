import unittest
from CalculadoraDescontoTDD import CalculadoraDescontoTDD


class TestCalculadoraDescontoTDD(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraDescontoTDD()

    def test_sem_desconto(self):
        resultado = self.calc.calcular_valor_final(200, False)
        self.assertEqual(resultado, 200)


if __name__ == "__main__":
    unittest.main