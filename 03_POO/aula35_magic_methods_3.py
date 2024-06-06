'''
 Python Special Methods, Magic Methods ou Dunder Methods
 Dunder = Doble Underscore = __dunder__
 
Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#specialnames
__lt__ (self, other) - self < other  (lt = less than)
__le__(self, other) - self <= other (le = less or equal)
__gt__(self, other) - self > other  (gt = greater than)
__ge__(self, other) - self >= other (gt = greater or equal)
__eq__(self, other) - self == other (eq = equal)
__ne__(self, other) - self != other (ne = not equal)
__sub__(self, other) - self - other (sub = subtrair)
__mul__(self, other) - self * other (mul = multiplicar)
__truediv__(self, other) - self / other (truediv = dividir)
__neg__(self) - - self (neg = negação aritimética)

Usaremos nessa aula:
__add__(self, other) - self + other (add = adicionar)
__gt__(self, other) - self > other (gt = greater than)

Já Usados:
__str__(self) - str (string)
__repr__(self) - str (repr = representação)
'''

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        class_name = type(self).__name__ # é a mesma coisa da linha de cima comentada
        return f'{class_name}(x= {self.x!r}, {self.y!r}, {self.z!r})' 
        
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultador_other = other.x + other.y
        return resultado_self > resultador_other # tomar cuidado com a posição
    
if __name__ == '__main__':
    p1 = Ponto(4, 2) # 6
    p2 = Ponto(6, 4) # 10
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que p2', p1 > p2)
    print('P1 é menor que p2', p2 > p1)