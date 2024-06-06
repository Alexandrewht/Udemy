'''
 Sempre que puder, conseguir e for possível
 eliminar os ifs e elses de uma função.
 
 Guard Clause
 
 'Cláusulas de proteção' são declarações condicionais usadas
 para retornar um valor assim que for determinado. 
 Na programação Python, eles são usados para evitar 
 aninhamentos desnecessários que poderiam tornar o código 
 menos legível e mais difícil de depurar. 
 Usar cláusulas de guarda é uma maneira prática de escrever 
 código Python mais limpo e eficiente.
'''

# Vamos utilizar a resolução do exercicio anterior para mostrar
import os

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
    listar(tarefas)
    
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Você não digitou nenhuma tarefa')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas')
    tarefas.append(tarefa)
    print()
    listar(tarefas)
    
def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas')
    tarefas.append(tarefa)
    print()
    listar(tarefas)
    
tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    
'''    if tarefa == 'listar':
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
        continue'''