# Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase

# Função que irá contar vogais e consoantes

def processar_frase(frase):
    frase_sem_espaco = frase.lower().replace(" ", "")
    
    # Contador de vogais e consoantes 
    
    vogais = []
    consoantes = []

    # Iterar sobre cada caractere da frase
    for caractere in frase_sem_espaco:
        if caractere in "aeiou":
            vogais.append(caractere)
        elif caractere.isalpha():
            consoantes.append(caractere)

    # Ordenar as listas alfabeticamente
    
    vogais.sort()
    consoantes.sort()

    # Imprimir as listas conforme pedido em atividade 
    
    print(f"Vogais: {vogais}")
    print(f"Consoantes: {consoantes}")


# Solicitar a frase do usuário

frase = input("Digite uma frase: \n")

# Processar a frase

processar_frase(frase)
