# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = {
    'nome': 'Alexandre',
    'sobrenome': 'white',
}
# a, b = pessoa.values()
# print(a, b)

# a, b = pessoa.items()
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

'''
 args e kwargs
 args (já vimos)
 kwags - keyword arguments (argumentos nomeados)
'''

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completas = {**pessoa, 'nome': 1, **dados_pessoa}

# print(pessoas_completas)

# empacotando
def mostro_argumentos_momeados(*args, **kwargs):
    print('Não nomeados:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)
    
mostro_argumentos_momeados(1, 2, nome='Aaa', qlq=123)
print()

# desempacotando
mostro_argumentos_momeados(**pessoas_completas)
print()

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_momeados(**configuracoes)