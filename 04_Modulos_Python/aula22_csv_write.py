# csv.writer e csvDictWriter para escrever em CSV
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula22.csv'

# lista de dicionários
lista_clientes = [
    {'Nome': 'Alexandre ', 'Endereço': 'Rua 2, 130'},
    {'Nome': 'Valéroa ', 'Endereço': 'Avenida Brasil, 44'},
    {'Nome': 'Maria ', 'Endereço': 'Avenida Brasil, 70'},
    {'Nome': 'Paulo ', 'Endereço': 'Rua 22, 33'}
]

'''# salvando em CSV
with open(CAMINHO_CSV, 'w', newline='', encoding='utf-8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    # nome_colunas = ['Nome', 'Endereço'] # também funciona da mesma forma
    escritor = csv.writer(arquivo)
    
    escritor.writerow(nome_colunas)
    
    for cliente in lista_clientes:
        escritor.writerow(cliente.values())'''

# salvando em CSV com dicionários
with open(CAMINHO_CSV, 'w', newline='', encoding='utf-8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()  # escreve o cabecalho

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)
