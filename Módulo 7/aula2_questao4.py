#Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
#Pelo menos 8 caracteres de comprimento.
#Contém pelo menos uma letra maiúscula e uma letra minúscula.
#Contém pelo menos um número.
#Contém pelo menos um caractere especial (por exemplo, @, #, $).

# Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
# Pelo menos 8 caracteres de comprimento.
# Contém pelo menos uma letra maiúscula e uma letra minúscula.
# Contém pelo menos um número.
# Contém pelo menos um caractere especial (por exemplo, @, #, $).

import re


def validador_senha(senha):
    # Requisitos mínimos de tamanho e caracteres
    if (
        len(senha) < 8
        or not re.search("[a-z]", senha)
        or not re.search("[A-Z]", senha)
        or not re.search("[0-9]", senha)
        or not re.search("[^a-zA-Z0-9]", senha)
    ):
        return False

    # Critério adicional (opcional)
    # Exemplo: verificar se a senha não contém palavras comuns do dicionário

    return True


# Obter a senha do usuário
senha = input("Digite sua senha: \n")

# Validar a senha e imprimir o resultado
if validador_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida. Certifique-se de que atenda aos critérios de segurança.")
