''' while/else'''
string = 'Valor qualquer'

# o comum é usar o i para o index
i = 0 # criando um index com a variável i

while i < len(string):
    letra = string[i]
    
# É possível procurar alguma coisa na string
# e pular o resto inclusive o else
    if letra == ' ':
        break
     
    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
    
print('fora do while.')