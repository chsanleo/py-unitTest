import math


# Listado de metodos definidos para operaciones matematicas basicas
def sumar(a, b): return a + b


def restar(a, b): return a - b


def doblar(a): return a * 2


def multiplicar(a, b): return a * b


def dividir(a, b): return a / b


def cuadrado(a): return pow(a, 2)


def raiz(a): return math.sqrt(a)


def es_par(a): return 1 if a % 2 == 0 else 0


# Metodo main para la validacion de los metodos
if __name__ == '__main__':
    print(sumar(3, 4, 9))
    print(doblar(3))
    print(es_par(3))
    print(cuadrado(3))
    print(raiz(22))
