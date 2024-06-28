''' Exemplo do uso dos sets
Obs. não será feito a válidação nesse exercicio
'''

letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())
    
    if 'l' in letras:
        print('PARABÉNS!')
        break
    
    print(letras)
    
    