# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. 
# Anagramas são palavras com os mesmos caracteres rearranjados.

# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo.
# Anagramas são palavras com os mesmos caracteres rearranjados.

from collections import Counter


def encontrar_anagramas(string, palavra_objetivo):
    # Contar as letras da palavra objetivo
    contagem_objetivo = Counter(palavra_objetivo)

    # Inicializar lista de anagramas
    anagramas_encontrados = []

    # Percorrer a string
    for i in range(len(string) - len(palavra_objetivo) + 1):
        # Contar as letras da substring atual
        contagem_substring = Counter(string[i : i + len(palavra_objetivo)])

        # Verificar se as contagens correspondem (anagrama)
        if contagem_objetivo == contagem_substring:
            anagramas_encontrados.append(string[i : i + len(palavra_objetivo)])

    # Retornar a lista de anagramas encontrados
    return anagramas_encontrados


# Obter a string e a palavra do usuário
string = input("Digite uma palavra: \n")
palavra_objetivo = input("Digite a palavra que deseja chegar: \n")

# Encontrar e imprimir anagramas
anagramas_encontrados = encontrar_anagramas(string, palavra_objetivo)

if anagramas_encontrados:
    print(f"Anagramas da palavra '{palavra_objetivo}' encontrados na string:")
    for anagrama in anagramas_encontrados:
        print(f"- {anagrama}")
else:
    print(f"Nenhum anagrama da palavra '{palavra_objetivo}' foi encontrado na string.")
