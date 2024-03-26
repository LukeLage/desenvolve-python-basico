num1 = float(input('Digite o primeiro número decimal:\n'))
num2 = float(input('Digite o segundo número decimal:\n'))

diferenca = num1 - num2
positivo = abs(diferenca)
decimal = round(positivo, 2)

print('A diferença absoluta entre esses dois números é de: \n{}'.format(decimal))