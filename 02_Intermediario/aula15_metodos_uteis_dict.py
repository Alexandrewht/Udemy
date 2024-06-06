'''
 Métodos úteis dos dicionários em Python
 (As marcações com asterisco são os temas falados nessa aula.)
 *len - quantas chaves 
 *keys - iterável com as chaves
 *values - iterável com os valores
 *items - iterável com chaves e valores
 *setdefault - adiciona valor se a chave não existe
 copy - retorna uma cópia rasa (shallow copy)
 get - obtém uma chave
 pop - apaga um item com a chave especificada (del)
 popitem - apaga o último item adicionado
 updade - atualiza um dicionário com outro
'''

''' indices repetidos
se houver indices repetidos será contado apenas uma vez.pessoa = {
    'nome': 'Alexandre',
    'sobrenome': 'white',
    'sobrenome': 'de',
    'sobrenome': 'mello',
}

No exemplo o sobrenome, será atualizado e irá mostrar apenas o último
'''

pessoa = {
    'nome': 'Alexandre',
    'sobrenome': 'white',
    'sobrenome1': 'de',
    'sobrenome2': 'mello',
    #'idade': 900,
}
# podem ser usados em exemplos de for com enumerate
for chave, valor in pessoa.items():
    print(chave, valor)

print('------len------') # Quantidade de índices
print(pessoa.__len__())
print(len(pessoa))

print('------keys------') # Nomes dos índices
print(list(pessoa.keys()))
print(tuple(pessoa.keys()))

print('------values------') # Valores dos índices
print(list(pessoa.values()))

print('------items-----') # índices e Valores
print(list(pessoa.items()))

print('------setdefault-----')
# Se houver uma idade já declarada não irá colocar o 0
# Se NÃO houver uma idade já declarada irá colocar o 0
pessoa.setdefault('idade', 0)
print(pessoa['idade'])