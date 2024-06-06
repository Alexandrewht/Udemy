'''
 Introdução ao desempacotamento
'''

# Precisa de ter o mesmo número de valores iteráveis
# Para cada valor vai em uma variável

nomes = ['Maria', 'Helena', 'Alexandre', 'Valéria']
nome1, nome2, nome3, nome4 = nomes 

print(nome2)

# Empacotando o resto dos valores
# Pode se usar qualquer variável para armazenar os valores
nome1, *resto = ['Maria', 'Helena', 'Alexandre', 'Valéria']
print(nome1)
print(resto)

# O método mais utilizado é o _
# O underline está sendo usado para armazenar os demais valores
_, nome2, *_ = ['Maria', 'Helena', 'Alexandre', 'Valéria']
print(nome2)

_, _, nome3, *_ = ['Maria', 'Helena', 'Alexandre', 'Valéria']
print(nome3)