'''
 datetime.tmedelta e deteutil.relativetimedelta (calculando datas)
 Docs:
 https://dateutil.readthedocs.io/en/stable/relativedelta.html
 https://docs.python.org/3/library/datetime.html#timedelta-objects
'''
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('23/05/2024 09:52:30', fmt)

# um time delta é a diferença entre duas datas
delta = timedelta(days=10, hours=-3)

#  é possível comparar datas 5
print(data_fim > data_inicio)
print(data_fim < data_inicio)
print(data_fim == data_inicio)
print('-' * 30)

print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(data_fim + delta)
print('-' * 30)

print(data_fim)
print(data_fim + relativedelta(seconds=60, minutes=10))

delta1 = relativedelta(data_fim, data_inicio)   
print(delta1)  # mostra o tempo da diferença entre as datas
print(delta1.days, delta1.years)  # 7 dias e 37 anos
