# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# uma classe pode gerar várias instâncias.
# na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
    
    
fusca = Carro('Fusca')
fusca.acelerar()

# a classe é um molde sem o conteúdo que precisa receber um método
Carro.acelerar(fusca) 
# print(fusca.nome)
# fusca.acelerar()
print()
    
celta = Carro('Celta')
celta.acelerar()
Carro.acelerar(celta)