'''
 @property - um getter no modo Pythônico
 getter - um método para obter um atributo
 cor -> get_cor()
 modo pythônico - modo do Python de fazer coisas
 
 @property é uma propriedade do objeto, ela
 é um método de que comporta como um atributo
 
 Geralmente é usada nas seguintes situações:
  - como getter
  - p/ evitar quebrar código cliente
  - p/ executar ações ao obter um atributo
  
  Código cliente - é o código que usa o seu código
'''

'''class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        
    # private protected public
    def get_cor(self):
        print('GET COR\n')
        return self.cor_tinta
    
############################################


caneta = Caneta('Azul')
print(caneta.get_cor())'''

############################################
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
       
    @property
    def cor(self):
        print('\nPROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456
        
caneta = Caneta('Azul')

print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)