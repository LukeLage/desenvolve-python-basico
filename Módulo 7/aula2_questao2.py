# Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

# Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".


def substituir_vogais(frase):
    # Vogais em minúsculo e maiúsculo
    vogais = "aeiouAEIOU"

    # Frase sem vogais
    frase_sem_vogais = ""

    # Percorrer cada caractere da frase
    for caractere in frase:
        # Verificar se o caractere é vogal
        if caractere in vogais:
            # Substituir vogal por "*"
            frase_sem_vogais += "*"
        else:
            # Adicionar outros caracteres à frase sem vogais
            frase_sem_vogais += caractere

    return frase_sem_vogais


# Obter a frase do usuário
frase = input("Digite a frase que deseja alterar: \n")

# Substituir vogais e imprimir resultado
frase_sem_vogais = substituir_vogais(frase)
print(f"Frase com vogais substituídas por '*': {frase_sem_vogais}")
