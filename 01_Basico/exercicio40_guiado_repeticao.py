'''
 Iterando strings com while
'''
#       0123456789
nome = 'Alexandre' # Iteráveis
# #       987654321 (negativos)
indice = 0
nome_intercalado = ''

while indice < len(nome):
    nova_string = '*'
    nome_intercalado += f'{nome[indice]}{nova_string}'
    indice += 1

print(nome_intercalado)

''' RESOLUÇÃO
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}'
    indice +=1

novo_nome += '*'
print(novo_nome)
'''