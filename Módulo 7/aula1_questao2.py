# Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. 
# Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.

nome = input('Digite o seu primeiro nome: \n')
sobrenome = input('Digite seu sobrenome: \n')

completo = nome + ' ' + sobrenome

print ('Seja bem vindo(a)', completo)