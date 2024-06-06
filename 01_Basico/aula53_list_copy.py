'''
 Cuidados com os dados mutáveis
 =  -> copiando o valor (imutáveis)
 =  -> aponta para o mesmo valor na memória (mutável)
'''

# Copiando valor
nome = 'Alexandre'

noutra_variavel = nome
print(nome)

nome = 'Aaaaaaa'
print(nome)
print(noutra_variavel)

'''
 Copiando a lista A para a lista B e
 mudando os valores de ambas
'''

# Apontando outro valor na memória
lista_a = ['Alexandre', 'Maria', 1, True, 1.2]
lista_b = lista_a
print(lista_b)

# Quando modificar a lista A, muda a lista B
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

'''
 Copiando a lista A para a lista B e 
 mudando os valores da lista A
'''

# É possível copiar a lista A, e modificar sem mecher na lista B
lista_a = ['Alexandre', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

# Quando modificar a lista A, não irá mudar a lista b
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
