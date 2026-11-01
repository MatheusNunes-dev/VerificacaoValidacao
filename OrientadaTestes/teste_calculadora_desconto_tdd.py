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


if __name__ == "__main__":
    unittest.main