# Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente).
# Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma.
# Seu programa deve continuar rodando até que o usuário digite "Fim"


def eh_palindromo(frase):
    # Remover espaços e pontuação
    frase_sem_formatacao = "".join(
        caractere.lower() for caractere in frase if caractere.isalnum()
    )

    # Verificar se a frase é igual ao seu inverso
    return frase_sem_formatacao == frase_sem_formatacao[::-1]


while True:
    # Obter a frase do usuário
    frase = input("Digite uma frase (ou 'Fim' para sair) para verificar se ela é palindromo: \n").lower()

    # Verificar se o usuário digitou "Fim"
    if frase == "fim":
        break

    # Verificar se a frase é um palíndromo
    if eh_palindromo(frase):
        print(f"A frase '{frase}' é um palíndromo!")
    else:
        print(f"A frase '{frase}' não é um palíndromo.")
