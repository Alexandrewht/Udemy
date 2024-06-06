'''
 Retorno de valores das funções (return)
'''
# None significa um não valor

variavel = print('Olá mundo') # None
#variavel = None
print(variavel)

def soma(x, y):
    if x > 10: # se a condição for verdadeira
        return 10, 20 
        # vai retornar aqui e não vai terminar o restante
    
    return x + y 
    ''' Se não tivesse o return a variavel global soma1 e 
    soma2 não seria possível fazer a soma entre eles
    pois retornaria TypeNone, com return
    passa a retornar um literal'''
    print(1 + 1) # A palavra return para tudo após ela 
                 # e não exibe o restante do escopo.
    
# variavel = soma(1, 2) #  None
# variavel = int('1')

soma1 = soma(2, 2) 
soma2 = soma(3, 3)
print(soma1)
print(soma2)

print(soma(11, 55)) # aqui retornou o if

'''LITERAIS EM PYTHON

Em Python, uma "literal" se refere a um valor que é 
inserido diretamente no código, sem a necessidade de cálculos 
ou avaliações. Em outras palavras, é um valor que representa 
a si mesmo e é usado para atribuir um tipo de dado específico 
a uma variável ou para realizar operações específicas. 
Existem vários tipos de literais em Python, 
cada um representando um tipo de dado diferente:
Literal numérico (int),
Literal de texto (str),
Litetal booleano (True/False),
Literal de Nenhum (None),
Literal de Sequência (lista e tuplas),
Literal de conjunto (elementos distintos {}),
Literal de bytes (sequência de bytes),
Literal de Expressão Regular (expressão regular),

Esses são alguns exemplos de literais em Python. 
Eles são usados para representar valores diretamente no código,
facilitando a atribuição e manipulação de dados.
'''