# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


# finally sempre vai ser executado.
# Exemplo de abrindo um arquivo e esquecendo de fechar
# else dificilmente vai ser usado no try
try:
    print('ABRIR ARQUIVO')
    8/0
    
# Pode se ter quantos except quiser
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')

except IndexError as error:
    print('Index error')
    
else:
    print('NÃO DEU ERRO')
        
finally:
    print('FECHAR AQUIVO')
    