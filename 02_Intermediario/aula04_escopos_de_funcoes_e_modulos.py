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

x = 1

'''
def escopo():
    x = 1
    print(x)

# print(x) # Não é possivel acessar a variável dentro da função
escopo()'''

# Outro exemplo

# É possível definir uma variável de modo global (fora da função)
# e chamar ela na função
def escopo():
    global x # Aqui tornamos o x global
    x = 10
    
    def outra_funcao(): # Pode também criar uma função dentro da função
        x = 4  # Este x esta dentro da função e não é global 
        y = 5  # O escopo, não pode acessar o y
        print(x, y)
        
    outra_funcao()
    print(x)

print(x)  
escopo()