'''
 dataclasses - O que são dataclasses?
 O módulo dataclasses fornece um decorador e funções para criar médotodos como
 __init__(), __repr__(), __eq__(), etc... em classes definidas pelo usuário.
 
 Em resumo: data classes são syntax sugar para criar classes normais.
 Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
 doc: https://docs.python.org/3/library/dataclasses.html
'''
from dataclasses import dataclass


@dataclass(init=False)  # init=False para que o __init__ seja ignorado
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    def __post_init__(self):
        print('POST INIT')


'''    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)'''


if __name__ == '__main__':
    p1 = Pessoa('Alexandre', 'white de mello')
    print(p1)
    print(p1.nome_completo)
