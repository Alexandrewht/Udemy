# Try, except, else e finally

try:
    a = 18
    b = 0
#    print('Linha 1'[1000]) # Index Error
#    print(b[0]) # Type Error.
    c = a / b # Aqui entra no except e o cód. abaixo não executa.
    print('Linha 2')
    
# aqui só vai entrar se houver erro de divisão por 0.
except ZeroDivisionError: 
    print('Dividiu por zero.')
    
# aqui só vai entrar se houver erro se a variavel não estiver declarada.     
except NameError:
    print('Nome b não está definido')
    
# é possível tratar mais de um erro.
except (TypeError, IndexError):
    print('TypeError + IndexError.')
    
# Exception é a classe que trata qualquer outro erro.
except Exception:
    print('ERRO DESCONHECIDO')
    
print('CONTINUAR')
    