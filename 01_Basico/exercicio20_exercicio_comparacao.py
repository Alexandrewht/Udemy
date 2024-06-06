"""
Deixar o usuário digitar 2 números e comprar eles 
para ver qual é maior 
Obs. o exercicio é treinar a lógica não precisa formatar em int
"""

primeiro = input('Digite um número: ')
segundo = input('Digite outro número: ')

if primeiro > segundo:
    print(f'O {primeiro} é maior que o {segundo}.')
elif segundo > primeiro:
    print(f'O {segundo} é maior que o {primeiro}.')
else:
    print('Os números são iguais.')


''' RESOLUÇÃO
primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

if primeiro_valor > segundo_valor:
    print(
        f'O {primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}.'
        )
else:
    print(
        f'O {segundo_valor=} é maior ou igual'
          f'ao que {primeiro_valor=}.'
          )
'''