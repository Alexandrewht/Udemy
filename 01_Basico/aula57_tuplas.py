'''
 Tipo tupla - uma lista imutável
'''

# Ao não colocar cochetes vai criar uma tupla
# Na tupla não é possível alterar o valor dentro

nomes = 'Maria', 'Helena', 'Alexandre', 'Valéria'
print(nomes[0])
print(nomes)

# fazendo a coerção de lista para tuple
nomes2 = ['Maria', 'Helena', 'Alexandre', 'Valéria']
nomes2 = tuple(nomes2)
print(nomes2)