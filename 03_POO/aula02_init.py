
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
            
p1 = Pessoa('Um nome', 'Qualquer')
#p1.nome = 'Um nome'
#p1.sobrenome = 'Qualquer'

p2 = Pessoa('Qualquer', 'Nome')
#p2.nome = 'Qualquer'
#p2.sobrenome = 'Nome'


print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)

