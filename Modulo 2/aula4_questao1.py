#Aqui irá ser adicionado o comprimento, largura do lote, além do preço por metro quadrado
comprimento = int(input('Digite aqui o comprimento do lote arredondado/inteiro: \n'))
largura = int(input('Digite aqui a largura do lote arredondado/inteiro: \n'))
preco = float(input('Digite aqui o preço do metro quadrado do lote: \n'))

#Duas fórmulas, a primeira irá calcular quantos metros quadrados o lote possui e o preço total dele
area_m2 = comprimento * largura
preco_total = preco * area_m2

#Função que irá imprimir o tamanho total em metros quadrados do lote e seu preço total
print('O terreno possui: ', area_m2, 'm2, e custa: R$', preco_total)