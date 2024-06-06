'''
 Cuidado com o ponto de vista
 Ao tentar importar um algo do modulo com import do modulo_b
 vamos gerar erro.'
'''

#  Aqui da erro ao tentar importar uma importação do modulo
#from packages_49.modulo import fala_oi


# o método de importar algo do modulo b
from package.modulo import fala_oi, soma_do_modulo

fala_oi()
print(soma_do_modulo(5, 7))
