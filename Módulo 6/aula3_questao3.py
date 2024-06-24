# Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del.
# Você deve imprimir a lista antes e depois da deleção.

# Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
#'Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

import random #Biblioteca que permitirá randomização

import random


def encontrar_e_remover_intervalo_negativo(numeros):

    # Inicializar variáveis
    inicio_intervalo_negativo = None
    fim_intervalo_negativo = None
    contagem_negativos_atual = 0
    contagem_negativos_maxima = 0

    # Percorrer a lista
    for i, numero in enumerate(numeros):
        # Verificar se o número é negativo
        if numero < 0:
            # Se for o primeiro número negativo
            if inicio_intervalo_negativo is None:
                inicio_intervalo_negativo = i
            # Atualizar a contagem de negativos
            contagem_negativos_atual += 1
        # Verificar se o número é positivo ou o fim da lista
        else:
            # Se for o fim de um intervalo negativo
            if inicio_intervalo_negativo is not None:
                # Atualizar a contagem máxima de negativos
                if contagem_negativos_atual > contagem_negativos_maxima:
                    contagem_negativos_maxima = contagem_negativos_atual
                    fim_intervalo_negativo = i - 1
                # Reiniciar a contagem de negativos
                contagem_negativos_atual = 0
                inicio_intervalo_negativo = None

    # Remover o intervalo negativo, se encontrado
    if fim_intervalo_negativo is not None:
        del numeros[inicio_intervalo_negativo : fim_intervalo_negativo + 1]


# Gerar lista aleatória
numeros = [random.randint(-10, 10) for _ in range(20)]

# Imprimir lista original
print(f"Lista original: {numeros}")

# Encontrar e remover intervalo negativo
encontrar_e_remover_intervalo_negativo(numeros)

# Imprimir lista editada
print(f"Lista editada: {numeros}")
