'''
 Exercício - Lista de tarefas com desfazer e refazer
 Música para codar :)
 Evereybody wants to rule the world - Tears of fears
 todo = [] -> lista de tarefas
 todo = ['fazer café'] -> adicionar fazer café
 todo = ['fazer café', 'caminhar'] -> adicionar caminhar
 desfazer = ['fazer café'] -> refazer ['caminhar']
 desfazer = [] -> refazer ['caminhar', 'fazer café']
 refazer = todo ['fazer café']
 refazer = todo ['fazer café, 'caminhar']
 
 escolher um dos comandos
 comandos: listar, desfazer, refazer
 input de adicionar tarefa ou escolher um comando
'''
import os
'''
tarefas = []
lista_armazenada = []

# listar os comandos
def listar(nome, lista):
    lista.append(nome)
    return lista

#remover ultimo
def remover(lista):
    if lista:
        return lista.pop()
    else:
        print('Lista vazia.')
        return None

#adicionando o ultimo que foi removido
def refazer(lista, lista_armazenada):
    if lista_armazenada:
        lista.append(lista_armazenada.pop())
    else:
        print('Nada para refazer.')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Escolha um dos comandos abaixo')
    print('Possíveis comandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa ou comando: ')

    if comando == 'listar':
        print('TAREFAS:', tarefas)
        
    elif comando == 'desfazer':
        removido = remover(tarefas)
        if removido is not None:
            lista_armazenada.append(removido)
    
    elif comando == 'refazer':
        
        refazer(tarefas, lista_armazenada)
    else:
        listar(comando, tarefas)
    
    input('Pressione qualquer tecla para continuar...')
    '''


# Resolução

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()
    
def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        return print('Nenhuma tarefa para desfazer')
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} foi removida da lista de tarefas')
    tarefas_refazer.append(tarefa)
    print()
    
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Você não digitou nenhuma tarefa')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas')
    tarefas.append(tarefa)
    print()
    
def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas')
    tarefas.append(tarefa)
    print()

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    
    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue