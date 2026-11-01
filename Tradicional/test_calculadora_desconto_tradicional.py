
import unittest
from Tradicional.CalculadoraDescontoTradicional import CalculadoraDescontoTradicional


class TestCalculadoraDescontoTradicional(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraDescontoTradicional()

    def test_sem_desconto(self):
        self.assertEqual(self.calc.calcular_valor_final(200, False), 200)

    def test_desconto_10_porcento(self):
        self.assertEqual(self.calc.calcular_valor_final(600, False), 540)

    def test_desconto_20_porcento(self):
        self.assertEqual(self.calc.calcular_valor_final(1200, False), 960)

    def test_desconto_vip(self):
        self.assertEqual(self.calc.calcular_valor_final(600, True), 513)

    def test_frete(self):
        self.assertEqual(self.calc.calcular_valor_final(80, False), 95)

    def test_frete_vip(self):
        self.assertEqual(self.calc.calcular_valor_final(100, True), 110)

    def test_valor_zero(self):
        with self.assertRaises(ValueError):
            self.calc.calcular_valor_final(0, False)

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.calc.calcular_valor_final(-50, False)

    def test_limite_500(self):
        self.assertEqual(self.calc.calcular_valor_final(500, False), 500)

    def test_limite_1000(self):
        self.assertEqual(self.calc.calcular_valor_final(1000, False), 900)


if __name__ == "__main__":
    unittest.main()
