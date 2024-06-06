# Operadores in e not in
# Strings em python são iteráveis
# significa que você pode navegar letra por letra
# ou número por número
#  0  1  2  3  4  5  6  7  8
#  A  l  e  x  a  n  d  r  e
# -9 -8 -7 -6 -5 -4 -3 -2 -1  

# in -> esta entre
# not in -> não esta entre

nome = 'Alexandre'
print(nome[3])

print(10 * '-')

print('á' in nome) 
print('al' in nome) # tem case sensitive
print('Al' in nome) 

print(10 * '-')

# not in inverte a situação
print('e' not in nome)
print('o' not in nome)

print(10 * '-')

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')