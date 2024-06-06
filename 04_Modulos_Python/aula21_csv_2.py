'''
 csv.reader e csv.DictReader
 csv.reader lê o CSV em formato de lista
 csv.DictReader lê o CSV em formato de dicionário
'''
from pathlib import Path
import csv
CAMINHO_CSV = Path(__file__).parent / 'aula20.csv'

'''# Abrindo como lista
    with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    # next(leitor)
    # print(next(leitor))
    for linha in leitor:
        # print(linha[1])
        print(linha)'''

# Abrindo como dicionário
with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereço'])
        # print(linha)