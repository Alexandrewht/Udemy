'''
 Dicionários em Python (tipo dict)
 Dicionários são estruturas de dados do tipo
 par de "chave" e "valor".
 Chaves podem ser condideradas como o "índice"
 que vimos na lista e podem ser de tipos imutáveis
 como: str, int, float, bool, tuple, etc.
 O valor pode ser de qualquer tipo, incluindo outro dicionário.
 Usamoas as chaves '{}' ou a classe dict para criar dicionários.
 Imutáveis: str, int, float, bool tuple
 Mutável: dict, list
 #Exemplo 1 Esse método é mais dificil de ler, mas tbm é usado
 para dicionários pequenos.
 pessoa = dict(nome='Alexandre', sobrenome='white de mello',
              idade='18', altura='1.75')
 
 #Exemplo 2 - Esse método é mais fácil de se ler.             
 pessoa = {
     'nome': 'Alexandre',
     'sobrenome': 'white de mello',
     'idade': '18',
     'altura': '1.75',
     'endereços': [
         {'rua': 'tal tal', 'numero': 123},
         {'rua': 'outra rua', 'numero': 321},
         {'rua': 'mais rua', 'numero': 312},
     ],
}
print(pessoa, type(pessoa))
'''

pessoa = {
    'nome': 'Alexandre',
    'sobrenome': 'white de mello',
    'idade': '18',
    'altura': '1.75',
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
        {'rua': 'mais rua', 'numero': 312},
    ],
}
#print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])