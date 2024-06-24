#Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 
#O primeiro passo é calcular o primeiro dígito verificador. 
# Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2.
#Em seguida somamos o resultado: 10+9+8+28+24+20+28+21+14 = 162
#Pegamos o resultado e dividimos por 11:  162 / 11 = 14 com resto 8
#Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
#Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).

# Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido".
# O primeiro passo é calcular o primeiro dígito verificador.
# Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2.
# Em seguida somamos o resultado: 10+9+8+28+24+20+28+21+14 = 162
# Pegamos o resultado e dividimos por 11:  162 / 11 = 14 com resto 8
# Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
# Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).


def validar_cpf(cpf_str):
    # Remover caracteres especiais
    cpf_sem_formatacao = cpf_str.replace(".", "").replace("-", "")

    # Verificar se o tamanho do CPF está correto
    if len(cpf_sem_formatacao) != 11:
        return False

    # Converter os dígitos em números
    try:
        cpf_numeros = [int(digito) for digito in cpf_sem_formatacao]
    except ValueError:
        return False

    # Calcular o primeiro dígito verificador
    soma_primeiros_nove = 0
    for indice, digito in enumerate(cpf_numeros[:9]):
        soma_primeiros_nove += digito * (10 - indice)
    resto_primeiro_digito = soma_primeiros_nove % 11
    primeiro_digito_verificador = (
        0 if resto_primeiro_digito < 2 else 11 - resto_primeiro_digito
    )

    # Calcular o segundo dígito verificador
    soma_com_primeiro_digito = 0
    for indice, digito in enumerate(cpf_numeros[:10]):
        soma_com_primeiro_digito += digito * (11 - indice)
    resto_segundo_digito = soma_com_primeiro_digito % 11
    segundo_digito_verificador = (
        0 if resto_segundo_digito < 2 else 11 - resto_segundo_digito
    )

    # Verificar se os dígitos verificadores conferem
    digitos_verificadores_conferem = (
        cpf_numeros[9] == primeiro_digito_verificador
        and cpf_numeros[10] == segundo_digito_verificador
    )

    return digitos_verificadores_conferem


# Obter o CPF do usuário
cpf_str = input("Digite seu CPF (XXX.XXX.XXX-XX): \n")

# Validar o CPF e imprimir o resultado
if validar_cpf(cpf_str):
    print("CPF válido!")
else:
    print("CPF inválido.")
