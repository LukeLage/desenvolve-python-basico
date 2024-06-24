#De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, contanto que a primeira e a última letra estejam no lugar correto. 
# Implemente uma função chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. 
# Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada. 
# Dica: use a biblioteca random.

# De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, contanto que a primeira e a última letra estejam no lugar correto.
# Implemente uma função chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis.
# Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada.
# Dica: use a biblioteca random.

import random


def embaralhar_palavras(frase):
    # Dividir a frase em palavras
    palavras = frase.split()

    # Embaralhar as letras internas de cada palavra
    for i, palavra in enumerate(palavras):
        if len(palavra) <= 2:
            continue

        # Separar a primeira e a última letra
        primeira_letra = palavra[0]
        ultima_letra = palavra[-1]

        # Embaralhar as letras do meio
        letras_meio = list(palavra[1:-1])
        random.shuffle(letras_meio)

        # Reconstruir a palavra embaralhada
        palavra_embaralhada = primeira_letra + "".join(letras_meio) + ultima_letra

        # Substituir a palavra original pela palavra embaralhada
        palavras[i] = palavra_embaralhada

    # Juntar as palavras embaralhadas em uma nova frase
    frase_embaralhada = " ".join(palavras)

    return frase_embaralhada


# Obter a frase do usuário
frase = input("Digite a frase a ser embaralhada: \n")

# Embaralhar as palavras e imprimir o resultado
frase_embaralhada = embaralhar_palavras(frase)
print(f"Frase embaralhada: {frase_embaralhada}")
