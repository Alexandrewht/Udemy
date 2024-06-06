# Notas das Exceptions (3.11.0)

class MeuError(Exception):
    ...
    
class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    # 1/0
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.add_note('Uma nota')
    exception_.__notes__ += error.__notes__.copy()
    exception_.add_note('Mais uma outra nota')
    raise exception_ from error 