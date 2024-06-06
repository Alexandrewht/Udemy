'''
 Imprecisão de ponto flutuante
 Double-Precision floating-point format IEEE 754
 https://en.wikipedia.org/wiki/Double-precision_floating-point_format
 https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
'''
import decimal

num1 = decimal.Decimal(0.1)
num2 = decimal.Decimal(0.7)
num3 = num1 + num2
print(num3)
print(f'{num3:.2f}')

# argumento 1 o numero, no argumento 2 as casas decimais
print(round(num3, 7))
# o round não trouxe os outros por serem zeros.
# ao usar decimal trouxe os zeros.

print(type(round))

num4 = decimal.Decimal('0.1')
num5 = decimal.Decimal('0.7')
num6 = num1 + num2
print(num6)