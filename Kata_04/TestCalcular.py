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
        """
        Test that it can sum a list of integers
        """
        result = Calc.sumar(8, 78)
        self.assertEqual(result, 86)
        print("test_suma -> OK")

    def tearDown(self):
        print("tearDown() -> OK")


if __name__ == '__main__':
    unittest.main()
