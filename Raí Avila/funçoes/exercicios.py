"""
Exercicio Aula 2
1/03/2024
Faça um programa que peça as três notas da disciplina (AP1, AP2 e AC) e mostre a média. 

"""

def calcular_media(ap1, ap2, ac):
    media = (ap1 + ap2) * 0.4 + ac * 0.2
    return media

ap1 = float(input("Digite a nota da AP1: "))
ap2 = float(input("Digite a nota da AP2: "))
ac = float(input("Digite a nota da AC: "))

media_notas = calcular_media(ap1, ap2, ac)

print("A média das notas é:", media_notas)

"""
Faça um programa que peça um comprimento em metros e converta para centímetros.

"""
def metros_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

comprimento_metros = float(input("Digite o comprimento em metros: "))

comprimento_centimetros = metros_para_centimetros(comprimento_metros)

print(f"{comprimento_metros} metros é igual a {comprimento_centimetros} centímetros.")
