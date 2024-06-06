# Manipulando chaves e valores em dicionários
pessoa = {}

## 
##

chave = 'nome'

# Criação do dicionário,
# Dicionário armazena uma coleção de dados imutáveis
pessoa[chave] = 'Alexandre'
pessoa['sobrenome'] = 'white'

# A lista funcionária da mesma forma
# Lista, armazena uma coleção de dados mutáveis 
lista = []

# mudando a chave para Maria
pessoa[chave] = 'Maria'

print(pessoa[chave])

# Deletando sobrenome
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# Utilizando um método dentro do Dicionário

''' get retorna None

print(pessoa.get('sobrenome'))
print(pessoa.get('sobrenome', 'Não existe'))

Obs. se não tivesse deletado o sobrenome, a linha 33 irá
trazer normalmente o sobrenome
'''

if pessoa.get('sobrenome', 'Não existe'): 
    print('Não existe')
else:
    print(pessoa['sobrenome'])


''' Outros Erros Comuns
 Se o dicionário estiver vazia e tentar puxar um índice que não tem,
 irá dar KeyRrror
 Se a lista estiver vazia e tentar puxar um índice que não tem,
 irá dar IndexError
 
#exemplos
pessoa['nome'] = 'Alexandre'
lista = []

print(pessoa)
print(lista[0])
print(pessoa['nome'])


O if também não busca valores dentro de dicionário se não houver.
Aqui o programa para e da KeyError
Resolução do possível problema na parte que explica o if.

if pessoa['sobrenome']:
    print('Existe')

print('ISSO Não vai')
'''
