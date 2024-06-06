'''
 Exercício com classes
 1- Crie uma calsse Carro (nome)
 2- Crie uma calsse Motor (nome)
 3- Crie uma calsse Fabricante (nome)
 4- Faça a ligação entre Carro tem um Motor
 Obs. Um motor pode ser de vários carros
 5- Faça uma ligação entre Carro e um Fabricante
 Obs. Um fabricante pode fabricar vários carros
 Exiba o nome do carro, motor e fabricante na tela
'''

'''class Carro:
    def __init__(self,nome ):
        self.nome = nome
        self.motor = []
        self.fabricante = []    
        
    def inserir_motor(self, motor):
        self.motor.append(Motor(motor))            
        
    def inserir_fabricante(self, fabricante):
        self.fabricante.append(Fabricante(fabricante))
        
    def listar_motor_e_fabricante(self):
        for motor in self.motor:
            for fabricante in self.fabricante:
                print(f'Motor: {motor.nome}, Fabricante: {fabricante.nome}')
        return ''
                        
class Motor:
    def __init__(self, nome):
        self.nome = nome
        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome

carro1 = Carro('Fusca')
carro2 = Carro('Palio')
carro3 = Carro('Uno')

carro1.inserir_motor('v1')
carro1.inserir_fabricante('Volkswagen')

carro2.inserir_motor('v2')
carro2.inserir_fabricante('Fiat')

carro3.inserir_motor('v3')
carro3.inserir_fabricante('Fiat 2.0')

print(carro1.nome)
print(carro1.listar_motor_e_fabricante())

print(carro2.nome)
print(carro2.listar_motor_e_fabricante())

print(carro3.nome)
print(carro3.listar_motor_e_fabricante())'''

# RESOLUÇÃO

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor
     
    @property 
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        
class Motor:
    def __init__(self, nome):
        self.nome = nome
        

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

# Carro 1      
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')

fusca.fabricante = volkswagen
fusca.motor = motor_1_0

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

# Carro 2
fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
motor_1_0 = Motor('1.0')

fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0

print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

# Carro 3
focus = Carro('Focus Titanium 2.0')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')

focus.fabricante = ford
focus.motor = motor_2_0

print(focus.nome, focus.fabricante.nome, focus.motor.nome)
