'''
 Combinations, Permutations e Product - Itertools
 Combinação - Ordem não importa - iterável + tamanho do grupo
 Permutação - Ordem importa
 Produto - Odem importa e repete valores únicos
'''
from itertools import combinations
from itertools import permutations
from itertools import product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
pessoas = [
    'Alexandre', 'Valéria', 'Maria', 'Paulo',
]
camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]


# combinations
print_iter(combinations(pessoas, 2))

# permutations
print_iter(permutations(pessoas, 2))

# product
print_iter(product(*camisetas))