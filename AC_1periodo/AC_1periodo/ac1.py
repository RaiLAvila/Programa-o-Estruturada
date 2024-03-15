"""
AC1 Exercicio 1: equações de segundo grau

"""

a = int(input("digite o valor de a:"))
b = int(input("digite o valor de b:"))
c = int(input("digite o valor de c:"))
delta = b**2 - 4*a*c
print("o valor de delta é:",delta)

x1 = (-b - delta**0.5) / (2*a)
x2 = (-b + delta**0.5) / (2*a)
print("O valor de x1 é:", x1)
print("O valor de x2 é:", x2)

"""
AC1 Exercicio 2: anos bissextos

"""
ano = int(input("Digite o ano: "))

bissexto = (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

print("O ano", ano, "é bissexto?" , bissexto)