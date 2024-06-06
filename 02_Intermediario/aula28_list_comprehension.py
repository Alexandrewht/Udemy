'''
 List comprehension em Python
 list comprehension é uma forma rápida para criar listas
 a partir de iteráveis.
'''

''' primeiro modo de gerar numeros de 0 a 10
print(list(range(10)))'''

# segundo modo de gerar numeros de 0 a 10
lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

# list comprehension
lista2 = [
    numero * 2 
    for numero in range(10)
]
print(lista2)

