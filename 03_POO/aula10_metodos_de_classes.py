'''
 Métodos de classe + factories (fábricas)
 São métodos onde "Self" será "cls", ou seja,
 ao invés de receber a instância no primeiro
 parâmetro, receberemos a própria classe.
'''
class Pessoa:
    ano = 2023 # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('João', 35)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(23)

print(Pessoa.ano)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
Pessoa.metodo_de_classe()