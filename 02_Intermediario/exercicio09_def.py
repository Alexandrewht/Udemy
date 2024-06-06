'''
 Exercícios com funções
 
 Crie uma função que multiplica todos os argumentos
 não nomeados recebidos
 Retorne o total para uma variável e mostre o valor
 da variável.

 Crie uma função fala se um número é par ou ímpar.
 Retorne se o número é par ou ímpar
'''

# Exercicio 1
def multi(*args):
    mutiplicador = 1
    for num in args: 
        mutiplicador *= num
    return mutiplicador

resultado = multi(10, 9)
print(resultado)

# Exercicio 2
def par_impar(x):   
    conta = x % 2 == 0
    if conta:
        print(f'O {x} é par')
    else:
        print(f'O {x} é ímpar')
    
par_impar(23)
par_impar(52)
par_impar(91)
par_impar(50)


'''RESOLUÇÃO EXERCICIO 1
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)'''

'''RESOLUÇÃO EXERCICIO 2
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    
print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))'''