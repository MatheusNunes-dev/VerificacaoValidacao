import unittest
from CalculadoraDescontoTDD import CalculadoraDescontoTDD


class TestCalculadoraDescontoTDD(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraDescontoTDD()


if __name__ == "__main__":
    unittest.main()