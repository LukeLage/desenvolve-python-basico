n = int(input('Digite a quantidade de experimentos: \n'))
contador = 0
cobaias = 0
ratos = 0
sapos = 0
coelhos = 0 

while contador < n:
    qnt_cobaias = int(input('Digite a quantidade de cobaias usadas nesse experimento: \n'))
    cobaias = input('Digite o código da cobaia: \n Ratos = R \n Sapos = S \n Coelhos = C \n')
    contador += qnt_cobaias
    cobaias_upper = cobaias.upper()
    if cobaias_upper == 'R': 
        ratos += qnt_cobaias
    elif cobaias_upper == 'S':
        sapos += qnt_cobaias
    else: 
        coelhos += qnt_cobaias

porcento_sapos = (sapos / contador) * 100
porcento_ratos = (ratos / contador) * 100
porcento_coelhos = (coelhos / contador) * 100

print('Total: {} cobaias' .format(contador))
print('Total de coelhos: {}' .format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}' .format(sapos))

print('Porcentual de sapos: {}'.format(porcento_sapos))
print('Porcentual de coelhos: {}'.format(porcento_coelhos))
print('Porcentual de sapos: {}'.format(porcento_sapos))