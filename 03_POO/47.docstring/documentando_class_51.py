"""Este é um módulo de exemplo.

 Este módulo contém funções e exemplos de documentação de funções.
 A função soma você hpa conhece bastante.
"""

variavel_1 = 1

class Foo:
    # def soma(x, y): 
    def soma(self, x: int | float, y: int | float) -> int | float:
        """
        Isso é a mesma coisa da função acima, mas com uma documentação
        Soma x e y
        
        :param x: Número 1
        :type x: int or float
        :param y: Número 2
        :type y: int or float
        
        :return: A soma entre x e y
        :rtype: int or float
        """
        return x + y

    def multiplica(
        self,
        x: int | float,
        y: int | float,
        z: int | float | None = None    
    ) -> int | float:
        """ Multiplica x, y e/ou z
        
        Multiplica x, y. SE o z for enviado, multiplica x, y, z
        """
        
        if z is None:
            return x * y
        return x * y * z

    def bar(self) -> int:
        """ O que ele faz
        
        ele levanta uma exceção
        :raises NotImplementedError: Se o método não for definido
        :raises ValueError: Se o valor não for definido
        """
        # O help, naõ vai retornar o erro, por isso a docstring ajuda a 
        # identificar e dar uma descrição sobre os erros
        raise NotImplementedError('Teste')

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4