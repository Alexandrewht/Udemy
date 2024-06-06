# EXCEPTIONS
# https://docs.python.org/3/reference/expressions.html#exception-raising-statements
# https://docs.python.org/3/reference/datamodel.html#emulating-exceptions
# https://docs.python.org/3/reference/datamodel.html#object.__exit__

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
        
        # raise class_exception(*exception_.args).with_traceback(traceback_)
        
        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        exception_.add_note('Uma nova nota')
        
        # return True # Tratei a exceção
        

with MyOpen('aula38.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
    