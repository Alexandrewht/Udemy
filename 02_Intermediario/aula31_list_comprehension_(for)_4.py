# primeiro modo de fazer a list comprehension
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

# segundo modo de fazer a list comprehension
lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)
]

# terceiro modo de fazer a list comprehension
lista = [
    [(x, letra) for letra in 'alexandre']
    for x in range(3)
]

print(lista)