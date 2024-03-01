"""
Programação Estruturada
01/03/2024
Funções
-encapsular uma informação
-isolar o comportamento para facilitar o uso 
-organizar o codigo
"""

#Declaração/ definição de função
def cabecalho():
    print("=" * 30)
    print("Relatório")
    print("=" * 30)

#Chamando uma função
cabecalho()
cabecalho()
cabecalho()


def cabecalho(título,sep):
    print(sep * 30)
    print(título)
    print(sep * 30)

cabecalho("Relatorio de despesas", "-")
cabecalho("Folha de pagamento", "=")


def cabecalho(título,sep, tamanho):
    print(sep * tamanho)
    print(título)
    print(sep * tamanho)

cabecalho("Relatorio de despesas", "=", 30)
cabecalho("Folha de pagamento", "=", 20)

def soma(a,b):
    return a + b

print(soma(2, 5) + soma(4, 9))

#Verificar se o numero é par ou impar
x= 2
print(x % 2 == 0)
def e_par(num):
    return num % 2 == 0

print(e_par(8))
print(e_par(9))