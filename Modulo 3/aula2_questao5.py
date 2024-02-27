genero = input('Digite seu genêro (M/F): \n')
idade = int(input('Digite a sua idade: \n'))
anos_servico = int(input('Digite quantos anos de serviço você possui: \n'))

if genero == 'F' and idade > 60:
    print('Essa pessoa já pode se aposentar? \n', True)
elif genero == 'M' and idade> 65:
    print('Essa pessoa já pode se aposentar? \n', True)
elif anos_servico > 30:
    print('Essa pessoa já pode se aposentar? \n', True)
elif idade > 60 and anos_servico > 25: 
    print ('Essa pessoa já pode se aposentar? \n', True)
else:
    print('Essa pessoa já pode se aposentar? \n', False)