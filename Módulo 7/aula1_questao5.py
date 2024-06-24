# Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. 
# Dica: letra in "aeiou". Exemplo:

# Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string.
# Dica: letra in "aeiou". Exemplo:


def contar_e_imprimir_vogais(frase):
    # Variaveis para contagem e armazenamento
    contagem_vogais = 0
    indices_vogais = []

    # Iterar sobre cada caractere da frase
    for indice, caractere in enumerate(frase.lower()):
        # Verificar se é vogal
        if caractere in "aeiou":
            # Contar a vogal
            contagem_vogais += 1
            # Adicionar o índice à lista
            indices_vogais.append(indice)

    # Imprimir os resultados
    print(f"A frase contém {contagem_vogais} vogais:")
    for indice in indices_vogais:
        print(f"- Vogais na posição {indice}: {frase[indice]}")


# Obter a frase do usuário
frase = input("Digite a frase que deseja verificar suas vogais: \n")

# Contar e imprimir as vogais
contar_e_imprimir_vogais(frase)
