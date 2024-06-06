'''
 Métodos úteis dos dicionários em Python
 (As marcações com asterisco são os temas falados nessa aula.)
 len - quantas chaves 
 keys - iterável com as chaves
 values - iterável com os valores
 items - iterável com chaves e valores
 setdefault - adiciona valor se a chave não existe
 copy - retorna uma cópia rasa (shallow copy)
 *get - obtém uma chave
 pop - apaga um item com a chave especificada (del)
 popitem - apaga o último item adicionado
 updade - atualiza um dicionário com outro
'''
p1 = {
    'nome': 'Alexandre',
    'sobrenome': 'white de mello',
}

print('------get------') # Pega o Valor
# Se não houver valor retorna None
print(p1.get('nome'))
print(p1.get('nome1')) # retorna None

# pode exibir algo, além de None
print(p1.get('nome1', 'Não existe')) # Aqui irá exibir Não existe

print('------pop------') # Apaga um item, com a chave especificada
nome = p1.pop('nome')
print(nome) # Aqui mostra o índice removido.
print(p1) # Aqui mostra a lista.

print('------popitem------') # Apaga o último elemento
sobrenome = p1.popitem()
print(sobrenome) # Aqui mostra o índice removido.
print(p1) # Aqui mostra a lista.

print('------update------') # Atualiza o dicionário
'''# fazendo update simples
p1.update(novo_nome='Alexandre', novo_sobrenome='white de mello')'''

'''# fazendo update com tupla
tupla = ('nome2', 'mais um valor'), ('outra idade', 30)
p1.update(tupla)'''

# fazendo update com dicionário
p1.update({
    'nome': 'Alexandre',
    'sobrenome': 'white de mello',
    'idade': '0990',
})

print(p1)