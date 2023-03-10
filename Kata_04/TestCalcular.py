import unittest
import Calcular as Calc


class TestCalcular(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass() -> OK")

    @classmethod
    def tearDown(cls):
        print("tearDownClass() -> OK")

    def setUp(self):
        print("setUp() -> OK")

    def test_suma(self):
        result = Calc.sumar(8, 78)
        self.assertEqual(result, 86)
        print("test_suma -> OK")

    def test_resta(self):
        result = Calc.restar(30, 15)
        self.assertEqual(result, 15)

    def test_doblar(self):
        result = Calc.doblar(15)
        self.assertEqual(result, 30)

    def test_multiplicar(self):
        result = Calc.multiplicar(9, 9)
        self.assertEqual(result, 81)

    def test_dividir(self):
        result = Calc.dividir(81, 9)
        self.assertEqual(result, 9)

    def test_cuadrado(self):
        result = Calc.cuadrado(11)
        self.assertEqual(result, 121)

    def test_raiz(self):
        result = Calc.raiz(121)
        self.assertEqual(result, 11)

    def test_esPar_par(self):
        result = Calc.es_par(99230390)
        self.assertTrue(result)

    def test_esPar_impar(self):
        result = Calc.es_par(778343)
        self.assertFalse(result)

    def tearDown(self):
        print("tearDown() -> OK")


if __name__ == '__main__':
    unittest.main()
