# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

# letras maiusculas e minusculas, digitos, pontuações
# print(s.ascii_letters, s.digits, s.punctuation)

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=255)))
random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([10, 11, 12]))

'''# Usando o secrets para fazer a mesma coisa que o random
# a aleatoriedade é maior já que não da para mudar a seed
# da aula 23

# Funções:
# seed
# -> NÃO FAZ NADA
random.seed(0)

# random.randrange(inicio, fim, passo)
# -> Gera um número inteiro aleatório dentro de um intervalo esperado.
r_range = random.randrange(10, 20, 2)
print(r_range)

# random.randint(inicio, fim)
# -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(inicio, fim)
# -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(r_uniform)

# random.shuffle(SequenciaMutável)
# -> Embaralha a lista original
nomes = ['Alexandre', 'Valéria', 'Maria', 'Paulo']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
# -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=2)
print(nomes)
print(novos_nomes)

# random.choices(Iterável)
# -> Escolhe um elemento iterável
choices = random.choices(nomes, k=2)
print(choices)

# random.choice(Iterável, k=N)
# -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
print(random.choice(nomes))
'''
