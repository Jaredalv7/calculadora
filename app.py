import calculator

print("Calculadora Simple")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma:", calculator.sumar(a, b))
print("Resta:", calculator.restar(a, b))
print("Multiplicación:", calculator.multiplicar(a, b))
print("División:", calculator.dividir(a, b))