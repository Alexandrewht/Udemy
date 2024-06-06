'''
 enumerate - enumera iteráveis (índices)
'''
#[(0, 'Maria'), (1, 'Helena'), (2, 'Alexandre'), (3, 'Valéria'), (4, 'João')]
lista = ['Maria', 'Helena', 'Alexandre', 'Valéria']
lista.append('João')

lista_enumerada = list(enumerate(lista))
# lista_enumerada = list(enumerate(lista, start=10))

print(lista_enumerada) # irá mostrar um iterator
print('------------')

for item in lista_enumerada:
    print(item)
print('------------')

# Não irá rodar novamente os valores que já foram utilizados
print('O que tem na lista enumerada: ', lista_enumerada)
for nada in lista_enumerada:
    print(nada)
print('------------')
'''  
# tem como fazer rodar novamente o enumerate

for nada in enumerate(lista):
    print(nada)
for nada in enumerate(lista):
    print(nada)
'''

# O Python automaticamente coloca o indice e nome
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
    
print('------------')  
for tupla_enumerada in enumerate(lista):
    print('FOR da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}') # \t da tab