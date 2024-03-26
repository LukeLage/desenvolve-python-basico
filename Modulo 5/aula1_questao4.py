from datetime import datetime

data = datetime.now()

data_atual = data.strftime('%d/%m/%Y')
hora_atual = data.strftime('%H:%M')
print('Data:', data_atual)
print('Hora:', hora_atual)