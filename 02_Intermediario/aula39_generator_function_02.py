'''
 Introdução às Generator functions em Python
 #generator = (n for n in range(1000000)
'''
# exemplo 1

def generator(n=0):
    print('Qualquer coisa aqui')
    print('E Aqui também')
    yield 1 # pausou aqui
    
    print('Continuando...')
    yield 2 # pausou aqui
    
    print('Vou terminar...')
    yield 3 # pausou aqui
    return 'ACABOU'

gen = generator(n=0)  
for n in gen:
    print(n)
    
# exemplo 2
print()

def generator2(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return
        
gen = generator2()
for n in gen:
    print(n)