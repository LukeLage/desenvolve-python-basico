#Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:
#A lista elementos
#A soma dos valores da lista
#A média dos valores da lista

import random #Biblioteca que fará o código capaz de gerar itens randomizados 

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range (num_elementos)] #Lista que irá gerar números aleatórios de acordo com o número aleatório de num_elementos

#Cálculos para encontrar a média

soma = sum(elementos)
media = soma / len(elementos)

#Impressões de acordo com o pedido pelas questões: 

print(
    'Lista criada: \n',
    elementos
)

print(
    'Soma dos valores da lista: \n',
    soma
)

print(
    'Média dos valores da lista: \n',
    media
)