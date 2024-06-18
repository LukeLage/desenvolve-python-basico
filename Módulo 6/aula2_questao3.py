#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
#Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
#Ambas as listas
#A lista intersecção ordenada
#A quantidade de vezes que cada elemento aparece em cada lista
#Atenção, a lista de intersecções não pode ter duplicatas.

import random #Bibliotecas que irão possibilitar randomização

#Listas com os 20 valores de 0 a 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint (0, 50) for _ in range(20)]

#Terceira lista com valores repetidos
interseccao = []

ordenada = sorted(interseccao)

#Funções que irão detectar esses valores repetidos
for elemento1 in lista1:
    if elemento1 in lista2:
        if elemento1 not in interseccao:
            interseccao.append(elemento1)

#Funções para encontrar quantas vezes um número se repete
contagem_interseccao = {}

def repeticao():
    for elemento, contagem in contagem_interseccao.items(): 
        print(f"{elemento}: {contagem}")

#Impressões de acordo com o pedido na questão
print(
    'Listas originais: \n',
    '1º: ', lista1, 
    '\n 2º: ', lista2
)

print(
    'Lista de intersecção ordenada: \n',
    interseccao
)

print(
    'Quantidade de vezes que o número se repete na intersecção: \n',
    repeticao()
)