# Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. 
# Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. 
# Adicione o separador "-" na sua impressão.

num = input('Digite o número do seu celular: \n')

# Função para impressão do número.

if len(num) == 8: # Detectar se o número tem 8 caracteres
    num = '9' + num
    num = num[0:5] + '-' + num[5:9]
elif len(num) == 9: # Detectar se o número tem 9 caracteres
    num = num[0:5] + '-' + num[5:9]

print(num)
