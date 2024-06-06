'''
Classe principal (Pessoa)
    -> super class, base class, parent class
    
Classes filhas (cliente)
    -> sub class, child class, derived class 
'''
'''class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        retorno = super().upper()
        print('DEPOIS DO UPPER')
        return retorno

string = MinhaString('Alexandre')
print(string.upper())'''

class A:
    atributo_a = 'valor A'
    
    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo(self):
        print('A')
        
class B(A):
    atributo_b = 'valor B'
    
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    
    def metodo(self):
        print('B')
        
class C(B):
    atributo_c = 'valor C'
    
    def __init__(self, *args, **kwargs):
        print('Ei, Burlei o sistema.')
        super().__init__(*args, **kwargs)
        
    def metodo(self):
        #super().metodo() # B
        #super(B, self).metodo() # A 
        #super(A, self).metodo() # object
        A.metodo(self)
        B.metodo(self)
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro()
      
c = C('Atributo', 'Qualquer')

# print(c.atributo)
# print(c.outra_coisa)

c.metodo()

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
