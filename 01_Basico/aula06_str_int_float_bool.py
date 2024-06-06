# conversão de tipos, coerção
# type conversion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos
# str, int, float, bool

print(1 + 1)
print('a' + 'b') # Polimorfismo, concatenou duas strings.
#print('1' + 1) # Aqui da erro, só pode concatenar str com str.
print()

print('conversão')
print('1', type('1'))
print(int('1'), type(int('1')))
print()

print(float('1') + 1)
print(type(float('1') + 1))
print()

print(bool(''))  # Sem espaço é Falso
print(bool(' ')) # Sem espaço é Verdadeiro
print()

print(str(11) + 'b')