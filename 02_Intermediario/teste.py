'''primeira = []
segunda = []
terceira = []

while True:
    e = int(input('Digite um valor para a primeira lista (0 para terminar): '))
    if e == 0:
        break
    primeira.append(e)

while True:
    e = int(input('Digite um valor para a segunda lista (0 para terminar): '))
    if e == 0:
        break
    segunda.append(e)

# Percorre os elementos da primeira lista
x = 0
while x < len(primeira):
    elemento = primeira[x]
    if elemento not in terceira:
        terceira.append(elemento)
    x += 1

# Percorre os elementos da segunda lista
x = 0
while x < len(segunda):
    elemento = segunda[x]
    if elemento not in terceira:
        terceira.append(elemento)
    x += 1

print(terceira)'''


