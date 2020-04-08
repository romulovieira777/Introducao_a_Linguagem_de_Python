# Curso de Introdução à Linguagem Python - Udemy

#Introdução
'''
print("Ola mundo!")
'''

#Comentários
'''
print("Outra mensagem")
print("Mensagem 3")
print("Nova linha")
'''

#Operações matemáticas
'''
print(2+2)
print(2-2)
print(2*2)
print(2/2)
print(2**3)
print(2//2)
print(2%2)
'''

#Variáveis
'''
minha_variavel = "Ola mundo!"
print(minha_variavel)
print(minha_variavel)
print(minha_variavel)
'''

'''
var1 = 1
var2 = 1.1
var3 = "Eu sou uma string"
var4 = True
var4 = False

print(var1)
print(var2)
print(var3)
print(var4)
'''

#Operadores Relacionais
'''
x = 2
y = 3

print(x == y)
print(x > y)
'''

#Operadores Lógicos
'''
x = 2
y = 3
soma = x + y

print(x==y and x == soma)
'''

'''
x = 3
y = 3
z = 3

print(x==y and x == z)
'''

#Comandos Condicionais
'''
#-*- coding: utf-8 -*-
x = 1
y = 10000000


if x > y:
    print("x é maior que y")

if y >x:
    print("y é maior que x")
'''

#Estruturas Condicionais (Comando else)
'''
#-*- coding: utf-8 -*-
x = 1
y = 2


if x > y:
    print("x é maior que y")

else:
    print("x não é maior que y")
'''

#Estruturas Condicionais (Comando elif)
'''
x = 1
y = 2

if x ==y:
    print("numeros iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("y maior que x")
else:
    print("numeros diferentes")
'''

#Estruturas de Repetição (Comando while)
'''
x = 1

while x < 100:
    print(x)
    x = x + 1
'''

#Estruturas de Repetição (Comando for)
'''
lista1 = [1,2,3,4,5]
lista2 = ["ola", "mundo","!"]
lista3 = [0, "ola", "biscoito", "bolacha", 9.999, True]

for i in lista3:
    print(i)
'''

#Estruturas de Repetição (Comandos for e range)
'''
for i in range(10):
    print(i)
'''

#Comando input
'''
numero = input("Digite um numero:")
print("O numero digitado eh:")
print(numero)
'''

'''
nome = input("Digite seu nome:")
print("Bem-vindo" + nome)
'''

#Strings parte 1
'''
a = "R"
b = "E"

concatenar = a +" "+ b
print(concatenar)

tamanho = len (concatenar)
print(tamanho)
'''

'''
a = "Rom"
b = "Edi"

concatenar = a +" "+ b
print(a[0])
'''

'''
a = "Rom"
b = "Edi"

concatenar = a +" "+ b
print(concatenar[0:6])
'''

#Strings parte 2
'''
a = "Rom"
b = "Edi"

concatenar = a +" "+ b + "\n"
print(concatenar)
print(concatenar.lower())
print(concatenar.upper())
print(concatenar.strip())
'''

'''
minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split("r")
print(minha_lista)
'''

'''
minha_string = "O rato roeu a roupa do rei de Roma"

busca = minha_string.find("rei")
print(busca)
'''

'''
minha_string = "O rato roeu a roupa do rei de Roma"

minha_string = minha_string.replace("o rei","a rainha")

print(minha_string)
'''

#Funções
'''
def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

s = soma(2, 3)
m = multiplicacao(3, 4)

print(soma(s, m))
'''

#Arquivos
'''
#para abrir arquivo utilizar open("nome do arquivo")

#para ler todas as linhas do arquivo nome do arquivo.readlines()

#para ler o arquivo todo, nome do arquivo.read() - o mais indicado é read.lines()
'''

#Listas parte 1
'''
minha_lista1 = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.89, True]
               
print(minha_lista1)
print(minha_lista2)
print(minha_lista3)                

for item in minha_lista1:
    print(item)

tamanho = len(minha_lista1)#saber o tamanho da lista
print(tamanho)

minha_lista1.append("limao")#para acrescentar item na lista
print(minha_lista1)

if 3 in minha_lista2:
    print("3 esta na lista")#saber o que está na lista

del minha_lista1[2:]#remover item da lista
print(minha_lista1)

minha_lista4 = []#criar uma nova lista
minha_lista4.append(57)
print(minha_lista4)
'''

#Listas parte 2
'''
lista = [124, 345, 5, 72, 46, 6, 7, 3, 1 , 7, 0]

lista.sort()#para ordenar crescente a lista
print(lista)

sorted(lista)
print(lista)

lista.sort(reverse = True)#para ordenar em ordem decrescente a lista
print(lista)

lista.reverse()#reverter a lista
print(lista)

lista2 = ["bola", "abacate", "dinheiro"]

lista2.sort()
print(lista2)

lista2.sort(reverse = True)
print(lista2)
'''

#Números aleatórios
'''
import random

random.seed(1)#para dar o mesmo resultado
numero = random.randint(0,10)#escolher numeros aleatorios
print(numero)
'''

#Tratamento de exceções
'''
a = 2
b = 0

try: #significa tentar fazer o print
    print(a/b)

except:
    print("Não é permitida divisão por 0")

print(a/b)
'''





























