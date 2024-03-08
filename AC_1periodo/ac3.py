"""
AC3 Exercicio 1: triângulos

"""
def determina_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo"
    elif a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4))
    print(determina_tipo_triangulo(2, 4, 4))
    print(determina_tipo_triangulo(3, 4, 5))
    print(determina_tipo_triangulo(1, 1, 4))
testa_triangulo()

"""
AC3 Exercicio 2: dia da semana

"""
def dia_semana(numero):
    if numero == 1:
        return "Domingo"
    elif numero == 2:
        return "Segunda-feira"
    elif numero == 3:
        return "Terça-feira"
    elif numero == 4:
        return "Quarta-feira"
    elif numero == 5:
        return "Quinta-feira"
    elif numero == 6:
        return "Sexta-feira"
    elif numero == 7:
        return "Sábado"
    else:
        return ""

def testa_dia_semana():
    print(dia_semana(2))
    print(dia_semana(6))
    print(dia_semana(7))
    print(dia_semana(9))
testa_dia_semana()

"""
AC3 Exercicio 3: calculadora simples

"""
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def calculadora():
    operacoes = {'soma': soma, 'subtracao': subtracao, 'multiplicacao': multiplicacao, 'divisao': divisao}

    while True:
        try:
            num1 = float(input("Informe um número: "))
            num2 = float(input("Informe outro número: "))
            operacao = input("Informe a operação (soma, subtracao, multiplicacao, divisao): ")

            if operacao.lower() in operacoes:
                resultado = operacoes[operacao.lower()](num1, num2)
                print("Resultado:", resultado)
            else:
                print("Operação inválida")
        except ValueError:
            print("Por favor, insira apenas números.")
calculadora()