'''
 Metaclasses são os tipos das classes
 EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
 Então, qual é o tipo de uma classe? (type)
 Seu objeto é uma instância de sua classe
 Sua classe é uma instância de type (type é um metaclass)
 type('Name', (Bases,), __dict__())
 
 Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
 __new__ da cçasse é chamado e cria uma nova classe
 __call__ da metaclass é chamado com os argumentos e chama:
    __new__ da class com os argumentos (cria a instância)
    __init__ da class com os argumentos
 __call__ da metaclass termina a execução
 
 Métodos importantes da metaclass
 __new__ (mcs, name, bases (heranças), dct) (cria a classe)
 __call__(cls, *args, **kwargs) (cria e inicializa a instância)
 
 "Metaclasses são magias mais profundas do que 99% dos usuários
 deviam se preocupar. Se você quer saber precisa delas,
 não precisa (as pessoas que realmente precisam delas sabem
 com certeza que precisam delas e não precisam de uma explicação
 sobre o porquê)."
 - Tim Peters (CPython Core Developer) 
'''

#object acima
# class Foo():
#     ...
    
Foo = type('Foo', (), {})
f = Foo()
#print(isinstance(f, Foo))
print(type(f))
print(type(Foo))
