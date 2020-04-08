#Exercícios da Udemy Python

#1_Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.
'''
idade = int(input("Digite sua idade:"))

if idade >=18:
    print("Maior de idade")

elif idade >0 and idade <18:
    print("Menor de idade")

else:
    print("Idade invalida")
'''

#2_Faça um programa que receba duas notas digitadas pelo usuário.
#Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
'''
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2)/2

print("Sua média é %f:" %(media))

if media >=6:
    print("Aprovado")

else:
    print("Reprovado")
'''

#3_Escreva um programa que resolva uma equação de segundo grau.
'''
import math
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

delta = (b**2) - 4*a*c
raiz_delta = math.sqrt(delta)

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print("x1 = %f" %x1)
print("x2 = %f" %x2)
'''

#4_Escreva um programa que ordene uma lista numérica com três elementos.   
'''
lista = [3,2,1]

lista = sorted(lista)
print(lista)
'''
'''
lista = [3,2,1]

for i in range(len(lista)):

    menor = i

    for j in range(i+1,len(lista)):
        if lista[j] < lista[menor]:
            menor = j
            
    if lista[i] != lista[menor]:
       aux = lista[i]
       lista[i] = lista[menor]
       lista[menor] = aux

print(lista)
''' 

#5_Escreva um programa que receba dois números e um sinal,
#e faça a operação matemática definida pelo sinal.
'''
num1 = input("Digite o primeiro número:")
operador = input("Digite o operador:")#preciso arrumar aqui para aceitar string
num2 = input("Digite o segundo número:")

if operador =="+":
    resultado = num1+num2

elif operador == "-":
    resultado = num1 - num2

elif operador == "/":
    resultado = num1 / num2

elif operador == "*":
    resultado = num1 * num2

elif operador == "%":
    resultado = num1 % num2

elif operador == "**":
    resultado = num1 ** num2

else:
    print("Operador inválido.")
    
print(resultado)
'''































