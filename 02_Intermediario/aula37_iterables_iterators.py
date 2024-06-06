'''
 Generator expression, 
 Iterables e Iterators em Python
'''
'''
 Iterator fornece uma maneira de acessar sequêncialmente
 os elementos de um objeto agregado sem expor
 sua representação subjacente.
 
 Ele não sabe nada sobre o iteravel, ele só sabe
 te entregar o próximo valor.
'''

iterable = ['Eu', 'Tenho', '__iter__']

# tem __iter__ e __next__
iterator = iter(iterable)
iterator2 = iterable.__iter__() 

print(iterable)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
