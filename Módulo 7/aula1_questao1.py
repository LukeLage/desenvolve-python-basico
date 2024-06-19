# Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.

nome = input('Digite seu nome: \n')
contador = ''

for letra in nome:
    contador += letra
    print(contador)
    
