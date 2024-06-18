# Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5,)

lista = []

# Função que irá juntar os números na lista

for i in range (5):
    num = int((input('Digite um número para ser adicionado na lista: \n')))
    lista.append(num)

# Função que irá separar os números pares e os números ímpares

pares = []
impares = []

for i in lista: 
    if i % 2: 
        impares.append(i)
    else:
        pares.append(i)

# Impressões conforme pedido em atividade

print(
    'Lista original: \n', 
    lista
)

print(
    'Os três primeiros elementos: \n',
    lista[:3]
)

print(
    'Os dois últimos elementos: \n',
    lista[3:]
)

print(
    'A lista invertida: \n', 
    lista [::-1]
)

print(
    'Os números pares: \n',
    pares
)

print(
    'Os números ímpares: \n',
    impares
)
