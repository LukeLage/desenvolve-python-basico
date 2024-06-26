# Escreva um script python que use compreensão de listas para criar as seguintes listas:
# Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
# Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
# Todos os números entre 1 e 100 que sejam divisíveis por 7
# Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento
# (ex: ['par', 'impar',… , 'impar'])


def gerar_listas():
    # 1. Números pares entre 20 e 50
    pares_20_50 = [numero for numero in range(20, 51, 2)]

    # 2. Quadrados dos valores de [1, 2, ..., 9]
    quadrados = [numero**2 for numero in range(1, 10)]

    # 3. Números divisíveis por 7 entre 1 e 100
    divisiveis_por_7 = [numero for numero in range(1, 101) if numero % 7 == 0]

    # 4. Paridade dos elementos em range(0, 30, 3)
    paridade = ["par" if elemento % 2 == 0 else "ímpar" for elemento in range(0, 30, 3)]

    return [pares_20_50, quadrados, divisiveis_por_7, paridade]


listas_geradas = gerar_listas()

for indice, lista in enumerate(listas_geradas):
    print(f"Lista {indice + 1}: {lista}")
