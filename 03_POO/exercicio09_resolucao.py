import json
from exercicio_salvando_class_em_JSON import CAMINHO_ARQUIVO, Pessoa, fazer_dump

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
    
if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()