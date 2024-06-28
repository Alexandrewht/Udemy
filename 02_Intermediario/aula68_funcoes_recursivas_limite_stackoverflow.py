'''
 Funções recursivas e recursividade
 - funções que podem se chamar de volta
 - úteis p/ dividir problemas grandes em partes menores
 
 Toda função recursiva deve ter:
 - Um problema que possa ser dividido em partes menores
 - Um caso recursivo que resolve o pequeno problema
 - Um caso base que para a recursão
 - fatorial - n!... 5! = 5 * 4 * 3 * 2 * 1 = 120
 https://brasilescola.uol.com.br/matematica/fatorial.htm
'''

'''import sys
sys.setrecursionlimit(1001) # não é recomendavel que passe muito além

def recursiva(inicio=0, fim=10):
    print(inicio, fim)
    
    # Caso base
    if inicio >= fim:
        return fim

    
    # caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

# Cuidado com o limite de recursos e funções de recursos
# o limite é 1000
print(recursiva(0, 100))'''

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
print(factorial(100))
# print(factorial(1000)) # problema no limite de recursão