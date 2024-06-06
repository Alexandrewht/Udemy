'''
 dataclasses - O que são dataclasses?
 O módulo dataclasses fornece um decorador e funções para criar médotodos como
 __init__(), __repr__(), __eq__(), etc... em classes definidas pelo usuário.
 
 Em resumo: data classes são syntax sugar para criar classes normais.
 Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
 doc: https://docs.python.org/3/library/dataclasses.html
'''
from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    p1 = Pessoa('Alexandre', 'White de mello')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])