# Métodos em instâncias de classes em Python
# o método init sempre retorna None
# Hard coded - é algo que foi escrito diretamente no código

'''class Carro:
    def __init__(self):
        self.nome = 'Fusca' # Hard coded,
    
fusca = Carro()
print(fusca.nome)

fusca = Carro()
print(celta.nome)'''

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
    
    def frear(self):
        print(f'{self.nome} está freando...')
    
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
fusca.frear()
print()
    
celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
celta.frear()
print()

print(fusca.nome.upper())
print(celta.nome.upper())