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
__str__(self) - str
__repr__(self) - str


__sub__(self, other): Método especial para subtração. Define o comportamento quando o operador de subtração (-) é usado com objetos da classe.
__mul__(self, other): Método especial para multiplicação. Define o comportamento quando o operador de multiplicação (*) é usado com objetos da classe.
__truediv__(self, other): Método especial para divisão real. Define o comportamento quando o operador de divisão (/) é usado com objetos da classe.
__floordiv__(self, other): Método especial para divisão de piso. Define o comportamento quando o operador de divisão de piso (//) é usado com objetos da classe.
__mod__(self, other): Método especial para o operador módulo. Define o comportamento quando o operador de módulo (%) é usado com objetos da classe.
__pow__(self, other): Método especial para potenciação. Define o comportamento quando o operador de potência (**) é usado com objetos da classe.
__eq__(self, other): Método especial para igualdade. Define o comportamento quando o operador de igualdade (==) é usado com objetos da classe.
__ne__(self, other): Método especial para desigualdade. Define o comportamento quando o operador de desigualdade (!=) é usado com objetos da classe.
__lt__(self, other): Método especial para menor que. Define o comportamento quando o operador de menor que (<) é usado com objetos da classe.
__le__(self, other): Método especial para menor ou igual a. Define o comportamento quando o operador de menor ou igual a (<=) é usado com objetos da classe.
__ge__(self, other): Método especial para maior ou igual a. Define o comportamento quando o operador de maior ou igual a (>=) é usado com objetos da classe.
__str__(self): Método especial para representação de string. Define o comportamento quando a função str() é chamada em um objeto da classe.
__repr__(self): Método especial para representação de string "oficial". Define o comportamento quando a função repr() é chamada em um objeto da classe.
__len__(self): Método especial para retorno do comprimento. Define o comportamento quando a função len() é chamada em um objeto da classe.
__neg__ (self): Método especial para negação. Define o comportamento quando o operador de negação (-) é usado para negação aritmética, ou seja, para inverter o sinal de um número.
__ne__ (self, other): Método especial para desigualdade. Ele é usado para verificar a desigualdade entre dois objetos. Ele é chamado quando você usa o operador de desigualdade (!=) entre dois objetos e retorna True se os objetos forem diferentes e False se forem iguais.
__add__(self, other): Este método especial é usado para definir o comportamento da adição (+) entre objetos da sua classe
__gt__ (self, other): Método especial para maior que. Define o comportamento quando o operador de maior que (>) é usado com objetos da classe.
__hash__ (self): Método especial para gerar um hash. Define o comportamento quando o método hash() é chamado em um objeto da classe.
'''