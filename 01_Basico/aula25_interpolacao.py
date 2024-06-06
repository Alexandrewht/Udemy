"""
 Interpolação básica de strings
 s - string
 d e o = int
 f - float
 x e X - Hexadecimal (0123456789ABCDEF)
 x minusculos gera letras minusculas, 
 X mausculas gera letras maiusculas 
"""

nome = 'Alexandre'
preco = 1000.957997
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)

print('O hexadecimal de %d é %04X' % (1500, 1500))