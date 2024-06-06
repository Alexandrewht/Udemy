'''
 Exercicio
 Exiba os índices da lista
 0 Maria
 1 Helena
 2 Alexandre
 3 Valéria
'''

lista = ['Maria', 'Helena', 'Alexandre', 'Valéria']

for nome in lista:
    print(lista.index(nome), nome, type(nome))

    
''' RESOLUÇÃO
listas = ['Maria', 'Helena', 'Alexandre', 'Valéria']
listas.append('João')


indices = range(len(listas))

for indice in indices:
    print(indice, listas[indice], type(listas[indice]))
'''