peso = int(input('Digite o peso do pacote em quilogramas: \n'))
distancia = int(input('Digite a distância de entrega em quilômetros: \n'))

if distancia <= 100 and peso <= 10:
    print('O valor que deve se pagar por um pacote de {} quilos em uma distância de {} quilômetros, é de: R$ {}'. format(peso, distancia, distancia))
elif distancia > 100 and distancia <= 300 and peso <= 10:
    preco = distancia * 1.5
    print('O valor que deve se pagar por um pacote de {} quilos em uma distância de {} quilômetros, é de: R$ {}'. format(peso, distancia, preco))
elif distancia > 300 and peso <= 10: 
    preco = distancia * 2
    print('O valor que deve se pagar por um pacote de {} quilos em uma distância de {} quilômetros, é de: R$ {}'. format(peso, distancia, preco))
elif distancia <= 100 and peso > 10:
    taxa = distancia + 10
    print('O valor que deve se pagar por um pacote de {} quilos em uma distância de {} quilômetros, é de: R$ {}'. format(peso, distancia, taxa))
elif distancia == 101 and distancia <= 300 and peso > 10:
    preco = distancia * 1.5
    taxa = preco + 10
    print('O valor que deve se pagar por um pacote de {} quilos em uma distância de {} quilômetros, é de: R$ {}'. format(peso, distancia, taxa))
elif distancia >= 300 and peso > 10: 
    preco = distancia * 2
    taxa = preco + 10
    print('O valor que deve se pagar por um pacote de {} quilos em uma distância de {} quilômetros, é de: R$ {}'. format(peso, distancia, taxa))
else: 
    print('Inválido')