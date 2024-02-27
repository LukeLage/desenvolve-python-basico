avaliacao = int(input('Digite a avaliação do filme: (1/5): \n'))

if avaliacao == 5:
    print('Excelente!')
elif avaliacao == 4:
    print('Muito Bom!')
elif avaliacao == 3: 
    print('Bom!')
elif avaliacao == 2:
    print('Regular')
else: 
    print('Ruim')