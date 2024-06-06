'''
 Generator expression (genexpr),
 são funções que sabem pausar.
 
 Iterator, tem a classe __iter__ e __next__
'''
import sys

iterable = ['Eu', 'Tenho', '__iter__']
# tem __iter__ e __next__
iterator = iter(iterable)


lista = [n for n in range(1000000)] # a lista está salva inteira na memória
# não existe tupla comprehension em python
generator = (n for n in range(1000000)) # objeto generator genexpr

# usando o sys pode-se verificar o tamanho do arquivo
print(sys.getsizeof(lista)) 
print(sys.getsizeof(generator))


# chamando o generator de um por um
print(next(generator))
print(next(generator))
print(next(generator))

# pode-se usar o for
for n in generator:
    print(n)
    
'''
 As vantagens da lista,
 como a lista inteira está na memória
 pode-se: acessar índice por índice, pode acessar qualquer índice,
 ultimo elemento, saber o tamanho da lista o que não ocorre com
 Generator, não tem como acessar len, não pode acessar índices,
 pois ele não está na memória, ele só sabe o próximo valor.
'''