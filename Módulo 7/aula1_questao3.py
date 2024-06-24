# Escreva um script que dado uma frase conta os espaços em branco.


def contar_espacos_em_branco(frase):
    contagem_espacos = 0
    for caractere in frase:
        if caractere == " ":
            contagem_espacos += 1
    return contagem_espacos


# Obter a frase do usuário
frase = input("Digite uma frase: \n")

# Contar os espaços em branco
numero_espacos = contar_espacos_em_branco(frase)

# Imprimir o resultado
print(f"A frase contém {numero_espacos} espaços em branco.")
