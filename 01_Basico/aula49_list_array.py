'''
 Listas em Python
 Tipo de list - Mutável
 Suporta vários valores de qualquer tipo
 Conhecimentos reutilizáveis - Índices e fatiamento
 Métodos úteis: append, insert, pop, del, clear, extend, +
'''

# list em python é o array
# A lista é mutável, é possível mudar o que tem dentro

#       + 01234
#       - 54321
string = 'ABCDE' # 5 caracteres (len)

# O comum é usar conchetes para criar uma lista
lists = []
print(bool(lists)) # falsy, precisa ter valores para ser verdadeiro.

# na lista é possível usar tudo, inclusive outra lista dentro da lista.

# Na lista é possível acessar cada elemento
# índice  0     1        2        3    4
#       - 5    -4       -3       -2   -1
lista = [123, True, 'Alexandre', 1.2, []]

# print(lista, type(lista))
print(lista)
print(lista[2], type(lista[2]))
print(lista[2].upper(), type(lista[2]))

# É possível mudar por ser mutável
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))