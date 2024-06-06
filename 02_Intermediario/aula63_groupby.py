# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Alexandre', 'nota': 'A'}, 
    {'nome': 'Valéria', 'nota': 'A'}, 
    {'nome': 'Maria', 'nota': 'A'}, 
    {'nome': 'Paulo', 'nota': 'A'}, 
    {'nome': 'Eduardo', 'nota': 'C'}, 
    {'nome': 'João', 'nota': 'B'}, 
    {'nome': 'André', 'nota': 'C'}, 
    {'nome': 'Anderson', 'nota': 'B'}, 
    {'nome': 'Fabrício', 'nota': 'D'}, 
    {'nome': 'Rose', 'nota': 'C'}, 
]

def ordena(aluno):
    return aluno['nota']


# lista tem sort, dicionário não tem sort
alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)


