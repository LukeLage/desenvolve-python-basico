idade = int(input('Digite sua idade: \n'))
jogos = input('Já jogou ao menos 3 jogos de tabuleiro? (sim/nao) \n') 
venceu = int(input('Digite quantos jogos você já venceu: \n')) 

if 16 <= idade <= 18 and jogos == 'sim' and venceu > 1:
    print('Apto para ingressar no clube de jogos de tabuleiro? True')
else: 
    print('Apto para ingressar no clube de jogos de tabuleiro? False')