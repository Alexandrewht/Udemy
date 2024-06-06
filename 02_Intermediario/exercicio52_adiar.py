'''
 Exercicio - Adiando a execução de funções
'''

def soma (x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, valor):
    def funcao_configurada(y):
        return funcao(valor, y)
    return funcao_configurada

try:
    numero = int(input('Digite um número: '))
except:
    print('Precisa ser um número')

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

resultado_soma = soma_com_cinco(numero)
resultado_multiplica = multiplica_por_dez(numero)

print(f'O resultado de {numero} + 5 = {resultado_soma}')
print(f'O resultado de {numero} * 10 = {resultado_multiplica}')


'''# Resolução

def soma (x, y):
    return x + y

def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

# Já armazenamos o x sendo 5
# Agora vamos puxar o y dentro da função interna

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
'''
