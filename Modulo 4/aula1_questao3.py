n1 = int(input('Digite o primeiro número: \n'))
n2 = int(input('Digite o segundo número: \n'))
n3 = int(input('Digite o segundo número: \n'))

m = (n1 + n2 + n3)/3

while m > 0:
    if m >= 60:
        print('Aprovado')
    elif m >= 40: 
        print('Recuperação')
    else:
        print('Reprovado')
    print('Fim')
    break