'''
 Maria pegou um empréstimo de 1.000.000
 para realizar o pagamento em 5 anos.
 A data em que ela pegou o empréstimo foi
 20/12/2020 e o vencimento de cada parcela 
 é no dia 20 de cada mês.
 - Crie a data do empréstimo
 - Crie a data final do empréstimo
 - Mostre todas as datas de vencimento e o valor
 de cada parcela
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta

'''#  pegando as datas
fmt = '%d/%m/%Y'
data_inicial = datetime(2020, 12, 20)
data_final = datetime(2025, 12, 20)


# subtraindo uma data de outra data
def meses(data_inicial, data_final):
    diferenca_anos = data_final.year - data_inicial.year
    diferenca_meses = data_final.month - data_inicial.month

    if diferenca_meses < 0:
        diferenca_anos -= 1
        diferenca_meses += 12

    return diferenca_anos * 12 + diferenca_meses

diferenca = meses(data_inicial, data_final)

#  formatando datas
data_inicial_fmt = data_inicial.strftime(fmt)
data_final_fmt = data_final.strftime(fmt)

#  valor do empréstimo
emprestimo = 1_000_000

print(f'Data inicial: {data_inicial_fmt}')
print(f'Data final: {data_final_fmt}')
print('-' * 30)

for i in range(diferenca):
    parcelas = emprestimo / diferenca
    meses_das_datas = data_inicial + relativedelta(months=i)
    print(f'parcela de N°: {i+1}')
    print(f'Data de vencimento: {meses_das_datas.strftime(fmt)}.')
    print(f'Valor da parcela: {parcelas:.2f}')
    print('-' * 40)
'''

# RESOLUÇÃO
valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)
    
numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas
 
for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:.2f}')
    
print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)