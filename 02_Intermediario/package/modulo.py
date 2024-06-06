'''
 Aqui estamos protegidos dentro do package,
 packages são usados para organizar os pacotes do import e outros
'''

# quando importa tudo *
# é possível só chamar oque estiver dentro do __all__
__all__ = [
    'varialvel',
    'soma_do_modulo',
    'nova_variavel'
]

varialvel = 'Alguma coisa'

def soma_do_modulo(x, y):
    return x + y

nova_variavel = 'Ookay.'


# Aqui vai dar erro de sem modulo nomeado, pois está sendo usado
# para ser saltado do modulo b para a aula 50
from package.modulo_b import fala_oi
