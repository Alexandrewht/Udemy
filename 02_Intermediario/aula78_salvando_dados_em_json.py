# Salvando Dados Python em Json
import json

pessoa = {
    'nome': 'Alexandre',
    'sobrenome': 'White de Mello',
    'enderecos': [
        {'rua': 'R1', 'numero': 25},
        {'rua': 'R2', 'numero': 52},
    ],
    'altura': 1.75,
    'numeros_preferidos': (2, 4, 5, 6, 7, 9, 10),
    'dev': True,
    'nada': None,    
}

with open('78.pessoa.json', 'w') as arquivo:
    json.dump(
        pessoa, 
        arquivo, 
        ensure_ascii=False,
        indent=2,
        sort_keys=True
              )