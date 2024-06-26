'''
  A, B, C, D
  D(B, C) - C(A) - B(A) - A

  método -> falar
        A
       / \
      B   C
       \ /
        D
        
 Para saber a ordem de chamada dos métodos
 Use o método de classe Classe.mro()
 Ou o atributo __mro__ (dunder - Double Underscore)
'''
class A:
    ...
    
    def quem_sou(self):
        print('A')
        
class B(A):
    ...
    
    # def quem_sou(self):
    #     print('B')
        
class C(A):
    ...
    
    def quem_sou(self):
        print('C')
        
class D(B, C):
    ...
    
    # def quem_sou(self):
    #     print('D')
        
d = D()
d.quem_sou()

print(D.mro())