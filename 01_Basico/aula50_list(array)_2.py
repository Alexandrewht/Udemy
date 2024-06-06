'''
 Listas em Python
 Tipo de list - Mutável
 Suporta vários valores de qualquer tipo
 Conhecimentos reutilizáveis - Índices e fatiamento
 Métodos úteis: 
    append, insert, pop, del, clear, extend, +
 Create Read Update    Delete -> (CRUD)
 Criar, Ler, Alterar,  Apagar = lista[i] 
'''

lista = [10, 20, 30, 40]
# é possível criar uma variável para pegar um valor
# numero = lista[2] 
print(lista[2])

lista[2] = 300
print(lista[2])

del lista [2]
# apartir daqui foi excluido o item 2 da lista
# e o python reorganizou e o indice 2 passou a ser 40.

print(lista)
print(lista[2])

# append adiciona novos valores ao final da lista
lista.append(30)
lista.append(50)
lista.append(60)
lista.append(70)
print(lista)

lista.pop() # O pop remove o ultimo elemento
# foi removido o 70
print(lista)

# É possível remover do meio da lista
ultimo_valor = lista.pop(3)
print(lista, 'Removido, ', ultimo_valor)