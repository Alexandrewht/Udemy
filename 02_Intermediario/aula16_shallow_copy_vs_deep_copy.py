'''
 Métodos úteis dos dicionários em Python
 (As marcações com asterisco são os temas falados nessa aula.)
 len - quantas chaves 
 keys - iterável com as chaves
 values - iterável com os valores
 items - iterável com chaves e valores
 setdefault - adiciona valor se a chave não existe
 *copy - retorna uma cópia rasa (shallow copy (cópia rasa))
 get - obtém uma chave
 pop - apaga um item com a chave especificada (del)
 popitem - apaga o último item adicionado
 updade - atualiza um dicionário com outro
'''
d1 = {
    'c1': '1',
    'c2': '2',
    'c3': '3',
    'l1': [0, 1, 2],
}
d2 = d1 # Aqui d2 aponta para o mesmo dicionario do d1
d2['c1'] = 1000 # Mudando o d2 c1 para 1000
print(d1) # O mesmo foi mudado para o d1

d1['c1'] = 1 # voltando o valor para 1

print('------copy------') # faz uma cópia rasa
# ele vai copiar tudo de um para o outro dicionário
d2 = d1.copy()

# porém se tiver algum valor alterado irá modificar os 2 dicionários 
# ambos os dois dicionários estão apontando o mesmo dicionário.
d2['l1'][1] = 9999999

print(d1)
print(d2)


print('------deepcopy------')
# o Python tem um módulo copy
import copy

d2 = copy.deepcopy(d1) 
# A partir desse modo será criado uma lista diferente para cada

d2['c1'] = 888888888
d1['c1'] = 'eeeeeeee'

print(d1)
print(d2)