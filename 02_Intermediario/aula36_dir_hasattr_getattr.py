# dir, hasattr e getattr em Python
string = 'Alexandre'
metodo = 'upper'
metodo1 = 'lower'
metodo2 = 'strip'

# Verificando se a string tem o método 'upper'
if hasattr(string, metodo):
    print('Existe upper')
    # Obtendo o valor da metodo 'upper'
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
    
'''
 Em resumo, dir é usado para listar atributos 
 de um objeto, hasattr para verificar 
 se um objeto tem um atributo específico 
 e getattr para obter o valor de um atributo 
 de um objeto. Essas funções são úteis para 
 inspecionar objetos e trabalhar com eles 
 dinamicamente.
 
 dir:
 A função dir é usada para listar os atributos 
 (métodos e variáveis) de um objeto em Python. 
 Isso pode ser útil para explorar as características 
 de um objeto, como uma classe, um módulo ou 
 uma instância de uma classe.
 
 hasattr:
 A função hasattr é usada para verificar 
 se um objeto tem um determinado atributo 
 (método ou variável) com um nome específico. 
 Retorna True se o atributo existir no objeto 
 e False caso contrário.
 
 getattr:
 A função getattr é usada para obter o valor 
 de um atributo de um objeto com base 
 no nome do atributo. Se o atributo existir, 
 seu valor será retornado.
'''