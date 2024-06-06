from functools import partial
from types import GeneratorType

# map - para mapear dados

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2) # round com 2 casas decimais

aumetar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

''' Novos produtos que já vimos
novos_produtos = [
    {**p, 'preco': aumetar_dez_porcento(p['preco'])} 
    for p in produtos
]'''

def muda_preco_de_produtos(produto):
    return {
        **produto, 
        'preco': aumetar_dez_porcento(
            produto['preco']
            )
        }
     
# usando o map com novos produtos
# Obs. map após percorrer a lista ou dicionario ela zera os dados
novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos    
))


print_iter(produtos)
print_iter(novos_produtos)

print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))

print(
    list(map(
            lambda x: x*3,
            [1, 2, 3, 4]
    ))
)