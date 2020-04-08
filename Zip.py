# Função Zip

lista1 = [1, 2, 3, 4, 5]
lista2 = ['abacate', 'bola', 'cachorro', 'elefante']
lista3 = ['R$ 2,00', 'R$ 5,00', 'Não tem preço', 'Não tem preço']

for numero, nome, valor in zip(lista1, lista2, lista3):
    print('{} {} {}'.format(numero, nome, valor))
