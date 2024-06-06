'''
 Introdução às funções (def) em Python
 Funções são trechos de código usados para
 replicar determinada ação ao longo do seu código.
 Elas podem receber valores para parâmetros (argumentos)
 e retornar um valor específico.
 Por padrão, funções em Python retornam None (nada).
'''

'''print('Olá mundo')

# Não utilizar letras maíusculas para criar a variável na função
# Exemplo mostrando que funciona, porém não é indicado.

def Print():
    print('Olá mundo!')
    print('Olá mundo!!!')
    
Print()'''

# parâmetros são definidos ao criar a função
def imprimir(a, b, c): # parâmetros a, b, c
    print(a, b, c)
    
# precisa de ter os argumentos de mesma quantia dos parâmetros
imprimir(1, 2, 3) # aqui é selecionado os argumentos

# é possível mudar os valores dos parâmetros
imprimir('e', 1, '6') # mudando o resutaldo para qualquer outro


def saudacao(nome='Sem nome!'):
    print(f'Olá, {nome}')

saudacao('Mario')
saudacao('José')
saudacao('Luiz')
saudacao()


