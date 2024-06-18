#Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 
#O primeiro passo é calcular o primeiro dígito verificador. 
# Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2.
#Em seguida somamos o resultado: 10+9+8+28+24+20+28+21+14 = 162
#Pegamos o resultado e dividimos por 11:  162 / 11 = 14 com resto 8
#Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
#Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
