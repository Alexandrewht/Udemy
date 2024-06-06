'''
 Python Special Methods, Magic Methods ou Dunder Methods
 Dunder = Doble Underscore = __dunder__
 
Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#specialnames
__lt__ (self, other) - self < other
__le__(self, other) - self <= other
__gt__(self, other) - self > other
__ge__(self, other) - self >= other
__eq__(self, other) - self == other
__ne__(self, other) - self != other
__add__(self, other) - self + other
__sub__(self, other) - self - other
__mul__(self, other) - self * other
__truediv__(self, other) - self / other
__neg__(self) - - self 

Usaremos nessa aula:
__str__(self) - str (string)
__repr__(self) - str (repr = representação)
'''

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __repr__(self):
        # class_name = self.__class__.__name__ 
        class_name = type(self).__name__ # é a mesma coisa da linha de cima comentada
        return f'{class_name}(x= {self.x!r}, {self.y!r}, {self.z!r})' 
        # !r (repr), é usada para mostrar o valor da variável
        
p1 = Ponto(1, 2)
p2 = Ponto(878, 776)

print(p1)
print(repr(p2))
print(f'{p1!r}')
