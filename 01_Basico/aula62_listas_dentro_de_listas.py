'''
 Lista de listas e seus índices
'''
salas = [
    #    0      1
    ['Maria', 'Helena', ],  # 0
    
    #  0
    ['Alexandre', ],  # 1
    
    #  0            1       2              3   
    #                             0  1   2    3   4
    ['Valéria', 'Luzia', 'João', (0, 10, 20, 30, 40)],  #  2
]
# mostrando as salas
print(salas)
print(salas[1])
print('-------------')

# buscando Luzia
print(salas[2][1])
print('-------------')

# buscando Helena
print(salas[0])
print(salas[0][1])
print('-------------')

# buscando João
print(salas[2])
print(salas[2][2])
print('-------------')

# buscando o 20 dentro da tupla
print(salas[2])
print(salas[2][3][2])
print('-------------')

# é possível fazer usando o for
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)