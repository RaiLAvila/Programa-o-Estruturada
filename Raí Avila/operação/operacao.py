"""
Programação Estruturada Aula 2
01/03/2024

Operaões em Python
Aritiméticas
Atribuição
Comparação
Lógicas
"""
#Operaçoes Aritiméticas(Números)
x= 10
y= 5

print(x + y) #Soma
print(x - y) #Subtração
print(x * y) #Multiplicação
print(x / y) #Divisão
print(x ** y) #Potência
print(x // y) #Divisão inteira
print(x % y) #Modulo

#round, número de digitos
print(round(x - y, 2))

#String
print("-" * 40) #Multiplicação de Strings

#Operações de Atribuição
x= 10
y= 10
w= 10
z= 10

x += 2 #x= x + 2
y -= 2 #y= y - 2
w *= 2 #w= w * 2
z /= 2 #z= z / 2
print(x)
print(y)
print(w)
print(z)

#Operações de Comparação
#Resultam em um valor Buleano(True ou False)

x= 10
y= 5
print(x > y)#maior que
print(x >= y)#maior ou igual a
print(x < y)#menor que
print(x <= y)#menor ou igual a
print(x == y)#igual a
print(x != y)#diferente de

#Operadores Lógicos
x= True
y= False
print(x and y)#E
print(x or y)#Ou
print(not x)#Não

#type casting
x= 9
print(float (x))
print(int("10"))

#Em python, tudo que for diferente de "", 0, 0.0, é True
print(bool(x))
print(bool(0))

print("abc" and 15)
print(0 and 15)
print(False and 15)
print("" and 15)

print("abc" or 15)
print(10.5 or 15)
print(True or 15)
print("" or 15)

print(5 or int("a"))

#Pythonica
nome = input("Inforime o seu nome:") or ("Valor invalido")

print(nome)

"""Precedência
()
**
*/ // %
* -
> >= < <= == !=
not
and
or
"""

print(6 + 3 * 2 <= 15 - 2.5 // 4% 3 and 10 / 2 or not 15 *2 ** 2 < 2)
print(6 + 3 * 2 <= 15 - 2.5 // 4% 3 and 10 / 2 or not 15 * 4 < 2)
print(6 + 6 <= 15 - 1.0% 3 and 5.0 or not 15 * 4 < 2)