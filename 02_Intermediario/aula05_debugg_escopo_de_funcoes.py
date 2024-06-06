'''
 Escopo de funções em Python
 Escopo significa o local onde aquele código pode atingir.
 Existe o escopo global e local.
 O escopo global é o escopo onde todo o código é alcançavel.
 O escopo local é o escopo onde apenas nomes do mesmo local
 podem ser alcançados.
 Não temos acesso a nomes de escopos internos nos escopos
 externos.
 A palavra global faz uma variável do escopo externo
 ser a mesma no escopo interno.
'''

# CallStack = pilha de chamadas

x = 1

def escopo():
    # global x 
    x = 10
    
    def outra_funcao():
        x = 11 # Se não tiver o x nesse escopo, 
        # irá buscar o x mais proximo
        # no caso esta buscando o x do escopo externo.
        y = 2 
        # global y # aqui da erro
        print(x, y)
        
    outra_funcao()
    print(x)

print(x) # De fora pra dentro não tem acesso, 
# mesmo que ela seja global 
escopo()
print(x)