"""
AC2 Exercicio 1: revisite a AC1

"""
#eq_seg_grau(a, b, c)

def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    x1 = (-b - delta**0.5) / (2*a)
    x2 = (-b + delta**0.5) / (2*a)
    return x1, x2

def main():
    a = float(input("Digite o valor de 'a': "))
    b = float(input("Digite o valor de 'b': "))
    c = float(input("Digite o valor de 'c': "))
    raiz1, raiz2 = eq_seg_grau(a, b, c)
    print("As raízes da equação são:", raiz1, "e", raiz2)

if __name__ == "__main__":
    main()
#bissexto(ano)
def bissexto(ano):
    return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

def main():
    ano = int(input("Digite o ano: "))
    resultado = bissexto(ano)
    if resultado:
        print("O ano", ano, "é bissexto.")
    else:
        print("O ano", ano, "não é bissexto.")
if __name__ == "__main__":
    main()

"""
AC2 Exercicio 2: salário

"""

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    salario_bruto = valor_hora * num_horas
    salario_liquido = salario_bruto * (1 - irpf)
    return salario_liquido

valor_hora = float(input("Digite o valor do salário por hora: "))
num_horas = float(input("Digite o número de horas trabalhadas no mês: "))

salario = calcula_salario(valor_hora, num_horas)
print("O salário líquido é:", salario)
