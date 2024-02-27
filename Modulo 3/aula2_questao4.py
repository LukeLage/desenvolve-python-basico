classe = input('Seu personagem é guerreiro, mago ou arqueiro? \n')
forca = int(input('Digite os pontos de força do seu personagem: (1 a 20) \n'))
magia = int(input('Digite os pontos de magia do seu personagem: (1 a 20) \n'))

if classe == 'guerreiro' and forca >= 15 and magia <= 10: 
    print('Pontos de atributo consistentes com a classe escolhida: ', True)
elif classe == 'mago' and forca <= 10 and magia >= 15:
    print('Pontos de atributo consistentes com a classe escolhida: ', True)
elif classe == 'arqueiro' and 5 <= forca <= 15 and 5 <= magia <= 15:
    print('Pontos de atributo consistentes com a classe escolhida: ', True)
else:
    print(False)
