import random
import math

quantidade = int(input('Digite quantos números aleatórios entre 0 e 100 você deseja: \n'))
contador = 0

for i in range(0, quantidade, 1):
    num = random.randint(1, 100)
    contador += num

raiz = math.sqrt(contador)

print('O valor da raiz quadrada dos números aleatórios é: {}'.format(raiz))
