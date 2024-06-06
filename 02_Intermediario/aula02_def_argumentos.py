'''
 Argumentos nomeados e não nomeados em funções Python
 Argumento nomeado tem nome com sinal de igual
 Argumento não nomeado recebe apenas o argumento (valor)
'''


def soma(x, y, z):
    # Definição da função
    print(f'{x=}, {y=}, {z=}', '|', 'x * y + z =', x * y + z)


# Execução da função

soma(1, 2, 3) # Argumento posicional
soma(3, 2, 1) # Invertendo a ordem pode fazer diferença

# Para inverter a ordem dos valores tem q mudar 
# o parâmentro no argumento.
soma(y=5, x=2, z=6)

soma(1, 2, z=8)
