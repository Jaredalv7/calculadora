import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import calculator


def test_sumar():
    assert calculator.sumar(2, 3) == 5


def test_restar():
    assert calculator.restar(5, 3) == 2


def test_multiplicar():
    assert calculator.multiplicar(4, 2) == 8


def test_dividir():
    assert calculator.dividir(10, 2) == 5