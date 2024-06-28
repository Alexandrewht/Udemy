'''
 Criando datas com módulo datetime
 datetime(ano, mês, dia)
 datetime(ano, mês, dia, horas, minutos, segundos)
 datetime.strftime('DATA', 'FORMATO')
 https://docs.python.org/3/library/datetime.html
'''
from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')

print(data.strftime('%d/%m/%Y'))  # só a data
print(data.strftime('%d/%m/%Y %H:%M'))    # só data e o horário hora e min.
print(data.strftime('%d/%m/%Y %H:%M:%S'))    # só data e o horário c/ segundos

print(data.strftime('%Y'), data.year)  # 2 modos de pegar o ano
print(data.strftime('%d'), data.day)  # 2 modos de pegar o dia  
print(data.strftime('%m'), data.month)  # 2 modos de pegar o mês  

print(data.strftime('%H'), data.hour)  # 2 modos de pegar a hora
print(data.strftime('%M'), data.minute)  # 2 modos de pegar o min.
print(data.strftime('%S'), data.second)  # 2 modos de pegar o sec.