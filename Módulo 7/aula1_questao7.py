# Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. 
# Regras:
# Chave de criptografia: gere um valor n aleatório entre 1 e 10
# Substitua cada caracter c pelo caracter c + n. 
# Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

# Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia.
# Regras:
# Chave de criptografia: gere um valor n aleatório entre 1 e 10
# Substitua cada caracter c pelo caracter c + n.
# Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

import random


def encrypt(lista_nomes):
    # Gerar chave aleatória
    chave_criptografia = random.randint(1, 10)

    # Criptografar cada nome
    lista_nomes_criptografados = []
    for nome in lista_nomes:
        nome_criptografado = ""
        for caractere in nome:
            # Substituir caractere por caractere + chave
            novo_caractere = chr(ord(caractere) + chave_criptografia)

            # Verificar se o novo caractere está no intervalo válido
            if 33 <= ord(novo_caractere) <= 126:
                nome_criptografado += novo_caractere
            else:
                # Se não estiver, usar o caractere original
                nome_criptografado += caractere

        # Adicionar nome criptografado à lista
        lista_nomes_criptografados.append(nome_criptografado)

    # Retornar nomes criptografados e chave
    return lista_nomes_criptografados, chave_criptografia


# Exemplo de uso
lista_nomes = ["João", "Maria", "Pedro"]
nomes_criptografados, chave = encrypt(lista_nomes)

print(f"Nomes criptografados: {nomes_criptografados}")
print(f"Chave de criptografia: {chave}")
