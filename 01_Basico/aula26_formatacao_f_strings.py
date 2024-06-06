"""
 Formatação básica de strings
 s - string
 d - int
 f - float
 x e X - Hexadecimal (0123456789ABCDEF)
 (Caractere) (><^)(quantidade)
 > - Esquerda
 < - Direita
 ^ - Centro
 = - Força o número a aparecer antes do zero
 Sinal - + ou 0
 Ex.: 0>-100,.1f
 Conversion flags - !r !s !a 
 !r - Chama o método __repr__
 !a - Chama o método __str__
 !a - Chama o método __ascii__
 vai ser explicado as conversion flags na aula de métodos
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{variavel:$^10}') # Mesmo mostrando erro ele coloca o cifrão

print(f'{1000.129317893712:+,.1f}')
# não precisa ficar querendo colocar virgula,
# que no proprio python tem bibliotecas que já preenche isso

print(f'{-1000.129317893712:0=+10,.1f}')

print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')