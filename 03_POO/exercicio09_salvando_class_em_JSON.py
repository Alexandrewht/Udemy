# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# faça em arquivos separados


'''import os
import json

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
def obter_dados():
    while True:
        nome = input("Digite seu nome: ")
        if nome.isalpha():  
            break
        else:
            print("Por favor, digite um nome válido.")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade > 0:  
                break
            else:
                print("Por favor, digite uma idade válida.")
        except ValueError:
            print("Por favor, digite um número inteiro para a idade.")
    
    while True:
        try:
            altura = float(input("Digite sua altura (em metros): "))
            if altura > 0:
                break
            else:
                print("Por favor, digite uma altura válida.")
        except ValueError:
            print("Por favor, digite um número para a altura.")

    return Pessoa(nome=nome, idade=idade, altura=altura)
    
def salvar(dados_pessoais, caminho):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_pessoais.__dict__, arquivo, indent=2, ensure_ascii=False)
 
def ler(dados_pessoais,caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print(dados)
    except FileNotFoundError:
        print('Arquivo não encontrado')
        salvar(dados_pessoais, caminho)
        
    
base = os.path.dirname(__file__)
caminho = os.path.join(base, '09.salvar_dados_pessoais_em_json.json')

while True:
        print('Comandos: \nSalvar para salvar, '
              '\nLer para ler, '
              '\nAdicionar para adicionar,'
              '\nSair para sair')
        comando = input('Digite um comando: ')
        
        if comando == 'salvar':
            salvar(obter_dados(), caminho)
        elif comando == 'ler':
            ler(obter_dados(), caminho)
        elif comando == 'sair':
            break'''
        
# RESOLUÇÃO
import json

CAMINHO_ARQUIVO = '09.resolução.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 35)
p3 = Pessoa('Joana', 35)
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)