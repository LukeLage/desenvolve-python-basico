#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
#A lista ordenada, sem modificar a lista original
# lista original
#O índice do maior valor da lista
#O índice do menor valor da lista

import random #Biblioteca que fará possível a randomização de números

numbers = [random.randint(-100, 100) for _ in range (20)] #Lista com os vinte números aleatórios e função que irá os aleatorizar

ordered_values = sorted(numbers)

#Impressão da lista de formas pedidas pela questão
print(
    'Lista ordenada: \n',
    ordered_values
)

print(
    'Lista original: \n',
    numbers
)

print(
    'Maior número da lista: \n',
    numbers.index(max(numbers))
)

print(
    'Menor número da lista: \n',
    numbers.index(min(numbers))
)
