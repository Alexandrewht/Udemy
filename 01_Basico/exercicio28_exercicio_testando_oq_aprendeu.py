"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
 Exiba:
   Seu nome é {nome}
   Seu nome invertido é {nome invertido}
   Seu nome contém (ou não) espaços
   Seu nome tem {n} letras
   A primeira letra do seu nome é {letra}
   A última letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "Desculpa, você deixou campos vazios."
"""

"""
 Aprendizagem do exercicio

 é possível criar variaveis com if, else
 mesmo elas dentro de um if
 
 não consigo substituir string por string

 .count conta a quantidade de caractere da str e armazena

 .replace substitui o valor antigo por um novo

 Eu tive que separar as letras dos espaços para poder fazer
 a verificação e soma deles e apresentar eles.
 
 Posso abrir um if dentro do if
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    verificar_espaco = 'contem' if ' ' in nome else 'não contem'
    numero_de_espacos = nome.count(' ')
    nome_sem_espaco = nome.replace(' ', '')
    
    numero_letras_no_nome = len(nome_sem_espaco)  
    nome_invertido = nome[::-1]
    ultima_letra = nome[-1]
    primeira_letra = nome[0]

    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido fica {nome_invertido}')
    print(f'O seu nome completo tem {numero_letras_no_nome} Letras')
    print(f'Em seu nome tem {numero_de_espacos} espaços')
    print(f'Seu nome tem {numero_letras_no_nome} letras')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A última letra do seu nome é {ultima_letra}')
else:
    print('Você precisa digitar um nome')


""" RESOLUÇÃO
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome não contem espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpa, você deixou campos vazios.')
"""