'''
 Iterável -> str, range, etc (__iter__())
 os dois underlines são chamados de dander.
 Iterador -> quem sabe entregar um valor por vez
 Next -> me entregue o próximo valor (__next__())
 Iter -> me entregue seu iterador
'''
texto = 'Alexandre' # iterável

'''
nome = iter('Alexandre') # __iter__()

print(texto.__next__())
print(next(texto))
'''

'''
# por baixo dos panos
iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
'''

# Oque foi feito acima.
for letra in texto:
    print(letra)