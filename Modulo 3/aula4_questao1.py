num1 = int(input('Digite o primeiro número: \n'))
num2 = int(input('Digite o segundo número: \n'))

soma = num1 + num2 
divisao = soma % 2

if divisao == 0 or divisao == 2:
    print('A soma dos números é par!')
else: 
    print('A soma dos números é impar')