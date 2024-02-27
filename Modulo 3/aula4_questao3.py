ano = int(input('Digite o ano que deseja verificar se é bissexto: \n'))

ano_4 = ano % 4
ano_400 = ano % 400
ano_100 = ano % 100

if ano_4 == 0 and ano_100 != 0:
    print('O ano {} é bissexto!' .format(ano))
elif ano_400 == 0:
    print('O ano {} é bissexto!' .format(ano))
else: 
    print('O ano {} não é bissexto!' .format(ano))