# A ordem é de dentro do parenteses para fora, os mais internos
# serão executados primeiro, o código é lido da esquerda para direita
# 1. (n + n)    parenteses
# 2. **         exponenciação
# 3. * / // %   multiplicação, divisão, divisão inteira, módulo
# 4. + -        adição, subtração

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

# É possível mudar o valor da variável
conta_1 = 'qualquer outra coisa'
print(conta_1)

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)