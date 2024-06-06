'''
 Crie funções que duplicam, triplicam e quadruplicam
 o número recebido como parâmetro.
'''

entrada = input('Digite um número: ')
numero = int(entrada) if entrada.isdigit() else None
 
def duplicar():
    dup = numero * 2
    return f'O {numero} duplicado é {dup}!'

def triplicar():
    trip = numero * 3
    return f'O {numero} triplicado é {trip}!'

def quadruplicar():
    mult = numero * 4
    return f'O {numero} quadruplicado é {mult}!'
 
print(duplicar())
print(triplicar())
print(quadruplicar())

'''# RESOLUÇÃO BÁSICA

def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadruplicar(numero):
    return numero * 4

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))'''

'''# RESOLUÇÃO 
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))'''
