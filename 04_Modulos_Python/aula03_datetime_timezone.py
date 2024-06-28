'''
 Criando datas com módulo datetime
 datetime(ano, mês, dia)
 datetime(ano, mês, dia, horas, minutos, segundos)
 datetime.strptime('DATA', 'FORMATO')
 datetime.now()
 https://pt.wikipedia.org/wiki/Era_Unix
 datetime.fromtimestamp(Unix Timestamp)
 https://docs.python.org/3/library/datetime.html
 para timezones
 https://www.wikipedia.org/wiki/List_of_tz_database_time_zones
 intalando o pytz
 pip install pytz types-pytz
'''
from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('America/Sao_Paulo'))
data1 = datetime.now(timezone('Europe/Paris'))
data2 = datetime(2024, 5, 23, 9, 40, 10, tzinfo=timezone('Europe/Paris'))

print(data)
print(data1)
print(data2)
print('-' * 40)
print(datetime.fromtimestamp(1716468136))  # Unix Timestamp

print(data.timestamp())  # Isso está na base de dados do Python