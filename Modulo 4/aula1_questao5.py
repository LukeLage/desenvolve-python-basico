contador = 0 
idades = 0 
n = int(input('Digite a quantidade de respondentes: \n'))


while contador < n: 
    idade = int(input('Digite a idade desse respondente: \n'))
    idades += idade
    contador += 1
    
media = idades / n
print(media)