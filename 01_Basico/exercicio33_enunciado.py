"""
Faça um programa que peça ao usuário digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um
número inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

if numero:    
    if numero.isdigit():
        numero_int = int(numero)
        
        if numero_int % 2 == 0:
            print('O número é par')
        else:
            print('O número é ímpar')
    else:
        print('Digite apenas números inteiros')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no
horário descrito, exiba a saudação apropriada. Ex.
Bom Dia 0~11, Boa Tarde 12~17 e Boa Noite 18~23
"""

hora = input('Digite que horas são: ')

if hora.isdigit():
    if hora:
        hora_int = int(hora)
        
        if hora_int <= 11:
            print('Bom dia')
        elif hora_int >= 12 and hora_int <= 17:
            print('Boa tarde')
        elif hora_int >= 18 and hora_int <= 23:
            print('Boa noite')
        else:
            print('Digite uma hora de 0 a 23')
    else:
        print('Digite apenas números de 0 a 23')
else:
    print('Digite apenas números.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome
tiver 4 letras o menos escreva "Seu nome é curto";
se tive entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite o seu nome: ')
qtd_letras = len(nome)

if qtd_letras > 1:
    if qtd_letras <= 4:
        print('O seu nomé é curto.')
    elif qtd_letras >= 5 and qtd_letras <= 7:
        print('O seu nome é normal.')
    else:
        print('O seu nome é muito grande.')
else:
    print('Por favor, digite alguma letra.')

''' RESOLUÇÃO EXERCICIO 1
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
        
    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro: ')
'''

''' RESOLUÇÃO EXERCICIO 2

entrada_hora = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada_hora)
    
    if hora >= 0 and hora <=11:
        print('Bom dia')
    elif hora >= 12 and hora <=17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora.')

except:
    print('Por favor, digite apenas números inteiros.')
'''

''' RESOLUÇÃO EXERCICIO 3
nome_letras = input('Digite seu nome: ')
tamanho_nome = len(nome_letras)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande')        
else:
    print('Por favor, digite alguma uma letra.')
'''