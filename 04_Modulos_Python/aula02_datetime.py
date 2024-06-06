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

data_str_data = '2022/04/20 07:49:23'
data_str_fmt = '%Y/%m/%d %H:%M:%S'

data_str_data_br = '19/04/2022 07:49:23'
data_str_fmt_br = '%d/%m/%Y %H:%M:%S'


# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
data1 = datetime.strptime(data_str_data_br, data_str_fmt_br)
print(data)
print(data1)