reais = int(input('Digite a quantidade em reais que deseja trocar: \n'))

notas_100 = reais // 100
reais %= 100

notas_50 = reais // 50
reais %= 50

notas_20 = reais // 20
reais %= 20

notas_10 = reais // 10
reais %= 10

notas_5 = reais // 5
reais %= 5

notas_2 = reais // 2
reais %= 2

notas_1 = reais // 1
reais %= 2

print ('{} Nota(s) de R$100: ' .format(notas_100))
print ('{} Nota(s) de R$50: ' .format(notas_50))
print ('{} Nota(s) de R$20: ' .format(notas_20))
print ('{} Nota(s) de R$10: ' .format(notas_10))
print ('{} Nota(s) de R$5: ' .format(notas_5))
print ('{} Nota(s) de R$2: ' .format(notas_2))
print ('{} Nota(s) de R$1: ' .format(notas_1))