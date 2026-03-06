import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import calculator

assert calculator.sumar(2, 3) == 5
assert calculator.restar(5, 3) == 2
assert calculator.multiplicar(4, 2) == 8
assert calculator.dividir(10, 2) == 5

print("Todas las pruebas pasaron correctamente ✅")