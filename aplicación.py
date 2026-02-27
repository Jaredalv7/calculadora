import calculator

print("Calculadora Simple")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma:", calculator.suma(a, b))
print("Resta:", calculator.resta(a, b))
print("Multiplicación:", calculator.multiplicacion(a, b))
print("División:", calculator.division(a, b))