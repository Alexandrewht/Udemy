'''
 Exercicio - usar o escopo do exercicio anterior e salvar
 a lista de afaseres em JSON
'''


import os
import json

'''def listar(tarefas):
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
BASE = os.path.dirname(__file__)
SALVAR = os.path.join(base, '82.salvando_em_json.json')


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
        with open(salvar, 'w') as arquivo:
            json.dump(tarefas, arquivo, indent=2,  encoding='utf-8')
        listar(tarefas)
        continue
    '''
    
''' CHAT GPT Com atualização direta no JSON, adicionando, refazendo e desfazendo tarefas


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer, arquivo):
    print()
    if not tarefas:
        return print('Nenhuma tarefa para desfazer')
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f'{tarefa=} foi removida da lista de tarefas e armazenada para refazer')
    
    # Atualizar o arquivo JSON
    salvar_tarefas(arquivo, tarefas)
    print()

def refazer(tarefas, tarefas_refazer, arquivo):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada de volta na lista de tarefas')
    
    # Atualizar o arquivo JSON
    salvar_tarefas(arquivo, tarefas)
    print()

def adicionar(tarefa, tarefas, arquivo):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas')
    tarefas.append(tarefa)
    
    # Atualizar o arquivo JSON
    salvar_tarefas(arquivo, tarefas)
    print()

def carregar_tarefas(arquivo):
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r') as arquivo_json:
                return json.load(arquivo_json)
        except json.JSONDecodeError as e:
            print(f"Erro ao carregar o arquivo JSON: {e}")
    return []

def salvar_tarefas(arquivo, tarefas):
    with open(arquivo, 'w') as arquivo_json:
        json.dump(tarefas, arquivo_json, indent=2)

tarefas = []
tarefas_refazer = []
base = os.path.dirname(__file__)
salvar = os.path.join(base, '82.salvando_em_json.json')

# Carregar tarefas ao iniciar
tarefas = carregar_tarefas(salvar)

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    
    if tarefa == 'listar':
        listar(tarefas)
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer, salvar)
        listar(tarefas)
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer, salvar)
        listar(tarefas)
    elif tarefa == 'clear':
        os.system('cls')
    else:
        adicionar(tarefa, tarefas, salvar)
        listar(tarefas)
'''


# RESOLUÇÃO

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


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('Arquivo não encontrado')
        salvar(tarefas, caminho_arquivo)
        
def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2,  ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = '82.resolução_exercicio_guardar_em_json.json'
tarefas = ler([], CAMINHO_ARQUIVO)
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
    salvar(tarefas, CAMINHO_ARQUIVO)
    