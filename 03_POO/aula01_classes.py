'''
 class - Classes são moldes para criar novos objetos
 As classes geram novos objetos (instâncias) que
 podem ter seus próprios atributos e métodos.
 
 Os objetos gerados pela classe podem usar seus dados
 internos para realizar várias ações.
 Por convenção, usamos PascalCase para nomes de classes.
'''

'''string = 'Alexandre' # str
print(string.upper())
print(isinstance(string, str))'''

class Pessoa:
    ...
    
p1 = Pessoa()
p1.nome = 'Um nome'
p1.sobrenome = 'Qualquer'

p2 = Pessoa()
p2.nome = 'Qualquer'
p2.sobrenome = 'Nome'


print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)