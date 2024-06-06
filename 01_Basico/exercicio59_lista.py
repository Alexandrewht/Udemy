'''
 Faça uma lista de comprar com listas
 O usuário deve ter a possibilidade de
 inserir, apagar e listar valores da sua lista
 Não permita que o programa quebre com
 erros de índices inexistentes na lista.
 '''

import os 
lista = []

while True:

    print('Selecione uma opção.')
    entrada = input('[i]nserir, [a]pagar, [l]istar: ')
    lista_add = ''
    lista_limite = len(lista)
    lista_rmv = ''
    indices = range(len(lista))
    
    if entrada.lower() == 'i':
        os.system('cls')
        lista_add = (input('Digite um valor: '))
        lista.append(lista_add)
        os.system('cls')
        
    elif entrada.lower() == 'a':
        try:
            lista_rmv = int(input('Digite um valor para deletar: '))
            
            if lista_limite >= 1:
                lista.pop(lista_rmv)
                os.system('cls')
            elif lista_limite == 0:
                print('Não há nenhuma lista')
                os.system('cls')
            else:
                os.system('cls')
                print('Você precisa digitar apenas números.')
        except:
            os.system('cls')
            print('Use o L para verificar a lista')
        
    elif entrada.lower() == 'l':
        os.system('cls')
        if lista_limite == 0:
            os.system('cls')
            print('Não há nada na lista.')
                
        for indices in lista:
            print(lista.index(indices), indices)
        
    else:
        print('Por favor digite "i" para inserir, "a" para apagar ou "l" para listar')


''' RESOLUÇÃO

import os
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite apenas números.')
        except IndexError:
            print('Não foi possível apagar este índice.')
        except Exception: # Mais utilizado, de forma genérica.
            print('Erro desconhecido.')
    
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nada para listar')
            
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
'''