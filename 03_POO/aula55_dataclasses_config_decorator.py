'''
 dataclasses - O que são dataclasses?
 O módulo dataclasses fornece um decorador e funções para criar médotodos como
 __init__(), __repr__(), __eq__(), etc... em classes definidas pelo usuário.
 
 Em resumo: data classes são syntax sugar para criar classes normais.
 Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
 doc: https://docs.python.org/3/library/dataclasses.html
'''
from dataclasses import dataclass


@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
