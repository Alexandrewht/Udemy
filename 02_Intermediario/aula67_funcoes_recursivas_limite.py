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

''' # RecursionError: maximum recursion depth exceeded

 Ocorre quando uma função está sendo chamada tantas
vezes que as invocações excedem o limite de recursão

 Para resolver o erro, especifique um caso base 
que deve ser atendido para sair da recursão ou 
defina um limite de recursão mais alto.

'''

def recursiva(inicio=0, fim=10):
    print(inicio, fim)
    
    # Caso base
    if inicio >= fim:
        return fim

    
    # caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())