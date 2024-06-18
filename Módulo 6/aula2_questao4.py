# Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores.
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista.
# Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
quantidade1 = int(input("Quantos números terão na primeira lista? \n"))
quantidade2 = int(input("Quantos números terão na segunda lista? \n"))

lista1 = []
lista2 = []


for i in range (quantidade1):
    num = int(input('Digite o número que deseja adicionar na primeira lista: \n'))
    lista1.append(num)

for i in range(quantidade2):
    num = int(input('Digite o número que deseja adicionar na segunda lista: \n'))
    lista2.append(num)

def combinar_listas(lista1, lista2):

    lista_combinada = []

    tamanho_minimo = min(len(lista1), len(lista2))

    for i in range (tamanho_minimo):
        lista_combinada.append(lista1[i])
        lista_combinada.append(lista2[i])
    
    if lista1 > tamanho_minimo:
        lista_combinada.extend(lista1[tamanho_minimo:])
    elif lista2 > tamanho_minimo:
        lista_combinada.extend(lista2[tamanho_minimo:])

lista_combinada = combinar_listas(lista1, lista2)
print('Lista combinada: ', lista_combinada)