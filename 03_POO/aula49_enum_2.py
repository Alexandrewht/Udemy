# Continuação da aula anterior
import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = 2
    ACIMA = 'posso por qualquer coisa aqui'
    ABAIXO = enum.auto()
    
    
print(Direcoes(1), Direcoes['ESQUERDA'])
print(Direcoes(1).name, Direcoes['ESQUERDA'].value)

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    
    print(f'Movendo para {direcao.name} ({direcao.value})')
    
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)