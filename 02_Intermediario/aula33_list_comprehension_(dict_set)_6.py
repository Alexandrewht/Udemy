# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# Dictionary comprehension

# for chave, valor in produto.items():
#     print(chave, valor)


dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

dc2 = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

dc ={
    chave: valor
    for chave, valor in lista
}

print(dict(lista))


# Set Comprehension

s1 = {i for i in range(10)}
print(s1)

# outro metodo
print(set(range(10)))

s2 = {2 ** i for i in range(10)}
print(s2)