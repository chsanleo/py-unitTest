import unittest


def doblar(a): return a * 2


def sumar(a, b): return a + b


class TextFixture(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto")
        self.r = []
        self.valores_a = [-3, -2, -1, 0, 1, 2, 3]
        self.valores_b = [-3, -2, -1, 0, 1, 2, 3]
        print("-> OK")

    def test_doblar(self):
        print("Realizando una prueba")
        r = [doblar(n) for n in self.valores_a]
        self.assertEqual(r, [-6, -4, -2, 0, 2, 4, 6])
        print("-> OK")

    def test_sumar(self):
        print("Realizando una prueba")
        # Obtenemos los valores en cada iteraccion
        for valor_a, valor_b in zip(self.valores_a, self.valores_b):
            self.r.append(sumar(valor_a, valor_b))

        self.assertEqual(self.r, [-6, -4, -2, 0, 2, 4, 6])

        print("-> OK")

    def tearDown(self):
        print("Destruyendo el contexto")
        del self.valores_a
        del self.valores_b
        del self.r

        print("-> OK")


if __name__ == '__main__':
    unittest.main()
