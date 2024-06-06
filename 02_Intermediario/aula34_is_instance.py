# isistance - para saber se o objeto é determinado tipo
# é instancia de
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Alexandre'},
]


for item in lista:
    if isinstance(item, set):
      #item. aqui após o ponto o python passa apenas os metodos do set
      print('SET')
      item.add(5)
      print(f'{item}, {isinstance(item, set)}\n')

    elif isinstance(item, str):
      #item. aqui após o ponto o python passa apenas os metodos da str
      print('STR')
      print(f'{item.upper()}, {isinstance(item, set)}\n')
      
    # quando é passado mais de um item (int, float), 
    # é chamado 'tipo int ou float'
    elif isinstance(item, (int, float)):
        print('NUM')
        print(f'{item}, {item * 2}\n')
    
    else:
        print('OUTRO')
        print(f'{item}\n')
    