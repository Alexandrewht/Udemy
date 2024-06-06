# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, c, *_, ap ,u = lista
print(a, u)

for nome in lista:
    print(nome, end=' ')
    
print(lista)
print(*lista)
print(*string)
print(*tupla)

# Dados da aula 62 para exemplo dessa aula
print('-------------')
salas = [
    #    0      1
    ['Maria', 'Helena', ],  # 0
    
    #  0
    ['Alexandre', ],  # 1
    
    #  0            1       2              3   
    #                             0  1   2    3   4
    ['Valéria', 'Luzia', 'João', (0, 10, 20, 30, 40)],  #  2
]

print(*salas)
print(*salas, end='\n')
print('-------------')
print(*salas, sep='\n')