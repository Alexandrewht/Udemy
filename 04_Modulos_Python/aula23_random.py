'''
 Random tem geradores de números pseudoaleatórios
 Obs.: números pseudoaleatórios significa que os números
 parecem ser aleatórios, mas na verdade não são. Portanto,
 este módulo não deve ser usado para segurança ou uso criptográfico.
 O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
 a saída pode ser previsível.
 doc: https://docs.python.org/3/library/random.html
'''
import random
# Funções:
# seed
# -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(0)

# random.randrange(inicio, fim, passo)
# -> Gera um número inteiro aleatório dentro de um intervalo esperado.
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(inicio, fim)
# -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(inicio, fim)
# -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# random.shuffle(SequenciaMutável)
# -> Embaralha a lista original
nomes = ['Alexandre', 'Valéria', 'Maria', 'Paulo']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
# -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=2)
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável)
# -> Escolhe um elemento iterável
choices = random.choices(nomes, k=2)
# print(choices)

# random.choice(Iterável, k=N)
# -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
# print(random.choice(nomes))
