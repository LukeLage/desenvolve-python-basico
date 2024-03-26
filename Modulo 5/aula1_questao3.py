import random

num = random.randint(1, 10)

while True: 
    chute = int(input('Faça um chute sobre o número aleatório: \n'))

    if chute > num: 
        print('Esse número é mais alto que o aleatório! Tente novamente!')
    elif chute < num: 
        print('Esse número é mais baixo do que o aleatório! Tente novamente!')
    elif chute == num:
        break

print("Correto! O número é: {}".format(num))
