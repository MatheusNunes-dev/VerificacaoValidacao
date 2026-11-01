import unittest
from CalculadoraDescontoTDD import CalculadoraDescontoTDD


class TestCalculadoraDescontoTDD(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraDescontoTDD()

    def test_sem_desconto(self):
        resultado = self.calc.calcular_valor_final(200, False)
        self.assertEqual(resultado, 200)

    def test_desconto_10_porcento(self):
        resultado = self.calc.calcular_valor_final(600, False)
        self.assertEqual(resultado, 540)
    
    def test_desconto_20_porcento(self):
        resultado = self.calc.calcular_valor_final(1200, False)
        self.assertEqual(resultado, 960)

    def test_desconto_vip(self):
        resultado = self.calc.calcular_valor_final(600, True)
        self.assertEqual(resultado, 513)
    
    def test_frete(self):
        resultado = self.calc.calcular_valor_final(80, False)
        self.assertEqual(resultado, 95)

    def test_valor_zero(self):
        with self.assertRaises(ValueError):
            self.calc.calcular_valor_final(0, False)

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.calc.calcular_valor_final(-50, False)


if __name__ == "__main__":
    unittest.main