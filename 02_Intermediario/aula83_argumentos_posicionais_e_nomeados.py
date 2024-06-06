'''
 Aula de como controlar os argumentos
 Controlando a quantidade de argumentos posicionais e nomeados
 em funções.
 *args (ilimitado de argumentos posicionais)
 **kwargs (ilimitado de argumentos nomeados)
 
 Positional-only Parameters (/) - Tudo antes da barra
 deve ser APENAS posicional
 PEP 570 - Python Positional-Only Parameters
 https://peps.python.org/pep-0570/
 Keyword-only Parameters (*) - * sozinho NÃO SUGA valores.
 PEP 613 - Python Keyword-Only Arguments
 https://peps.python.org/pep-3102/
'''

def soma(a, b, /, x, y):
    print(a + b + x + y)
    
soma(1, 2, y=3, x=4)


def subtracao(a, b, *, c):
    print()
    print(a - b - c)
    
subtracao(10, 5, c=1)


def divisao(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a / b / c)
     
divisao(10, 5, c=1, nome='teste')