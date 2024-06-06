'''
 Context Manager com classes
 Você pode implementar seus próprios protocolos
 apenas implementando os dunder methods que o 
 Python vai usar.
 Isso é chamado de Duck typing. um conceito
 relacionado com tipagem dinâmica onde o Python não
 está interessado no tipo, mas se alguns métodos existentes
 no seu objeto para que ele funcione de forma adequada.
 Duck Typing: 
 Quando vejo um pássaro que caminha como um pato, 
 nada como um pato, grasna como um pato, eu chamo aquele pássaro
 de pato.
 Para criar um context manager, os métodos __enter__ e __exit__
 devem ser implementados.
 O método __exit__ receberá a classe de exceção, a exceção e o 
 traceback. Se ele retornar True, exceção no with será suprimidas.
'''

# with open('aula37.txt', 'w') as arquivo:
#     ...

# OBSERVAÇÃO: o Windows não vem com o encoding, por isso, coloque o utf8
'''
class MyContextManager:
    def __init__ (self):
        print('INIT')
    
    def __enter__(self):
        print('ENTER')
        return 1234
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('EXIT')
        
instancia = MyContextManager()

with instancia as alguma_coisa:
    print('WITH', alguma_coisa)
'''
    
class MyOpen:
    def __init__ (self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo =  open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
        
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

with MyOpen('aula37.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.write('Caminhão (sem o utf 8, estaria outra coisa inelegível)\n')
    print('WITH', arquivo)
    