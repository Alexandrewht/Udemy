"""
Fatiamento de strings
índices de Olá mundo: 
 0  1  2  3  4  5  6  7  8
 O  l  á     m  u  n  d  o
-9 -8 -7 -6 -5 -4 -3 -2 -1

Fatiamento [i:f:p] [::]
i - inicio, f - final, p - pula
Obs.: a função len retorna a qtd
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4]) # Aqui só pega o índice 4

# Aqui pega do índice 4 até o 8, 
# vai mostrar oque está entre eles
print(variavel[4:8])

print(variavel[4:]) # Aqui pega do índice 4 até o final
print(variavel[:5]) # Aqui pega do inicio até o índice 5

print(variavel[-8:-2])

print(variavel[3]) # Cuidado com os espaços

# LEN
# A função Len, conta caracteres da string
# Len começa a contagem do 1.

print(variavel[0:len(variavel):5])
print(variavel[0:9:1]) # Aq foi solicitado para ir do 0 ao 9, sem pular casas
print(variavel[0:9:2]) # Aq foi solicitado para ir do 0 ao 9, pulando 2 casas
print(variavel[0:9:3]) # Aq foi solicitado para ir do 0 ao 9, pulando 3 casas

print(variavel[::-1]) # Aq foi solicitado para ir do -1 ao -9, de forma invertida
print(variavel[-1:-10:-1]) # Aq é outro exemplo