'''
args - Argumentos não nomeados
 - *args (empacotamento e desempacotamento)
'''

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

# args é uma Tupla
def soma(*args):
    print(args)
    total = 0
    for numero in args:
        total += numero
    return total

outra_soma = soma(*numeros) # desempacotamento
print(outra_soma)

print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10)))