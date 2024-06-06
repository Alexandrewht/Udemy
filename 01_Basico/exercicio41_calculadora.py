'''
 Calculadora com while
 1. pedir um número
 2. pedir outro número
 3. permitido apenas + - * /
'''

# criar um modo de sair (concluido)
# pedir para digitar numeros (concluido)
# verificar erros de digitação dos n1 e n2 (concluido)
# verificar erros de digitação do operador (concluido)

while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Digite um dos operadores (+-/*): ')
    operador_permitidos = '+-/*'

    if operador_permitidos:
        try:
            n1 = float(n1)
            n2 = float(n2)
        except:
            print('Você precisa digitar um número.')
            continue

        if operador == '+':
            print(f'A soma de {n1} + {n2} é : ', n1 + n2)
        elif operador == '-':
            print(f'A subtração de {n1} - {n2} é : ', n1 - n2)
        elif operador == '/':
            print(f'A divisão de {n1} / {n2} é : ', n1 / n2)
        elif operador == '*':
            print(f'A multiplicação de {n1} * {n2} é : ', n1 * n2)
        else:
            print('Você precisa escolher apenas um dos operadores entre (+ - / *).')

    else:
        continue

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
    
     
''' USANDO EVAL
expressao_matematica = input('Digite uma expressão matemática: ')
resultado = eval(expressão_matematica)
print('O resultado é', resultado)
'''


''' RESULTADO
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    num_1_float = 0
    num_2_float = 0
    numeros_validos = None
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
#   pode ser usado para visualisar o erro e tratar dele.
#   except Exception as error:
#       print(error)    
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo.')
    if operador == '+':
        print(f'a soma do {num_1_float}+{num_2_float} é =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'a subtração do {num_1_float}-{num_2_float} é =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'a divisão do {num_1_float}/{num_2_float} é =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'a multiplicação do {num_1_float}*{num_2_float} é =', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.') # Se chegar aqui algo deu errado.
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
#    sair.lower() # está fazendo o Sair ficar com o 'S' minusculo
#    sair.startswith('s') # está verificando se começa com 's' 
    if sair is True:
        break
'''