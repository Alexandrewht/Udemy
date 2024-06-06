"""
 Exercício - Unir listas
 Crie uma função zipper (como o zipper de roupas)
 O trabalho dessa função será unir duas listas na ordem.
 
 Use todos os valores da menor listas.
 
 Ex.:
 ['Salvador', 'Ubatuba', 'Belo Horizonte']
 ['BA', 'SP', 'MG', 'RJ']
 resultado
 [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]     
"""

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def unir(**args):
 
    ziper = zip(l1, l2)
    for i in ziper:
        print(i)
    return ziper

unir()


'''# SOLUÇÃO 1

def zipper(lista1, lista2):
    intervalo_minimo = min(len(l1), len(l2))

    return [
        (lista1[i], lista2[i]) for i in range(intervalo_minimo)
    ]
    
print(zipper(l1, l2))'''


'''# SOLUÇÃO 2

print(list(zip(l1, l2)))'''


'''# SOLUÇÃO 3
from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))'''
