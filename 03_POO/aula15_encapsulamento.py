'''
 Encapsulamento (modificadores de acesso: public, protected, private)
 Python NÃO TEM modificadores de acesso
 Mas podemos seguir as seguintes convenções:
  (sem underline) = public
       pode ser usado em qualquer lugar
  (com underline) = protected
        não DEVE ser usado fora da classe
        ou suas subclasses.
  (dois underlines) = private
        "name mangling" (configuração de nomes) em Python
        _NomeClass__nome_attr_ou_method
        só DEVE ser usado na classe que foi declarado.
'''
from functools import partial


class Foo:
      def __init__(self):
            self.public = 'isso é publico'
            self._protected = 'isso é protegido'
            self.__private = 'isso é privado'
        
      def metodo_public(self):
            # self._metodo_protected()
            # print(self._protected)
            print(self.__private)
            self.__metodo_private()
            return 'metodo_public'
      
      def _metodo_protected(self):
            print('_metodo_protected')
            return '_metodo_protected'
      
      def __metodo_private(self):
            print('__metodo_private')
            return '__metodo_private'
      
      
f = Foo()
print(f.metodo_public())
print(f._Foo__metodo_private())

