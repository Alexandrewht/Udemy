'''
 Usando calendar para calendários e datas
 https://docs.python.org/3/library/calendar.html
 Com calendar, você precisa saber coisas como:
 - Qual o útilmo dia do mês (ex.: monthrange)
 - Qual o nome e números de dia de determinada data (ex.: weekday)
 - Criar um calendário em si (ex.: monthcalendar)
 - Trabalhar com coisas especificas de calendários (ex.: calendar, month)
 Por padrão dia da semana começa em 0 até 6
 0 = segunda-feira | 6 = domingo
'''
import calendar
print(calendar.calendar(2024))  # calendário de 2024
print(calendar.month(2024, 12))  # calendário de 12/2024

print('-' * 100)
# O primeiro dado na tupla é o valor do dia 0 até 6
# O segundo dado na tupla é o ultimo dia do mês (12)
print(calendar.monthrange(2024, 12))
print(list(enumerate(calendar.day_name)))

print('-' * 100)
# essas variaveis pega o primeiro e o segundo dado do range
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2024, 12)

print(calendar.day_name[numero_primeiro_dia])
print(calendar.weekday(2024, 12, ultimo_dia))
print(calendar.day_name[calendar.weekday(2024, 12, ultimo_dia)])

print('-' * 100)
for week in calendar.monthcalendar(2024, 12):
    for day in week:
        if day == 0:
            continue
        print(day, sep='-', end=' ')
