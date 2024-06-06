'''
vídeo expilicando oque é Json e mostrando exemplos
 https://www.youtube.com/watch?v=XmCrArtfjaQ
'''

''' Oque é Json e sua praticidade

 O JSON (JavaScript Object Notation) 
 é um formato de dados usado para transmitir 
 e armazenar dados de forma organizada e legível 
 por máquinas. 
 Ele é baseado na sintaxe de objetos JavaScript 
 e é amplamente utilizado em APIs para enviar 
 e receber dados entre diferentes sistemas.

 E essa estrutura de dados é super simples
 ela é similar a um dicionário em python.
 A linguagem JSON é bastante usada, por oferecer 
 simplicidade, legibilidade, portabilidade 
 e suporte amplo, o que a torna uma 
 escolha assertiva para a troca de informações 
 na web e em outros ambientes.

 Além disso, existem inúmeras outras razões 
pelas quais o JSON é amplamente utilizado. 
Confira algumas delas a seguir:

 Simplicidade: o formato JSON é relativamente 
simples e fácil de entender. 
Ele usa uma sintaxe leve e minimalista, 
tornando-o rápido de ser processado;

 Legibilidade: o JSON é projetado para ser legível 
tanto por humanos quanto por máquinas. 
Sua estrutura é organizada e fácil de analisar, 
facilitando a depuração de erros e o trabalho 
das pessoas desenvolvedoras;

 Portabilidade: ele é independente de plataforma 
e pode ser utilizado em diferentes linguagens 
de programação. Isso facilita o compartilhamento 
de dados entre sistemas heterogêneos, tornando 
o processo mais eficiente;

 Suporte amplo: a mai parte das linguagens de 
programação possui suporte nativo ou bibliotecas 
que facilitam a manipulação de dados em formato 
JSON. Isso torna mais simples o processo de 
codificação e decodificação de JSON em objetos 
ou estruturas de dados;

 Integração com a web: o JSON é muito utilizado na 
comunicação entre servidores e clientes em 
aplicações web, inclusive em APIs 
(Interface de Programação de Aplicativos), para 
transferir dados entre servidor e clientes de 
forma mais eficiente.
'''

''' Anotações

 O Arquivo Json não recebe comentários
 
 comentários anotados sobre a vídeo aula
 
 O JSON suportam os seguitnes tipos de daos
 boolean, 
 number (int ou float), 
 null, 
 string, 
 array [] (grupo de valores)
 objeto {}

 no json usamos aspas duplas "nome"
 
 o json é usado para recebermos respostas
 
'''

import json
import os 

pessoas = [
    {"nome": "Alexandre", 
    "sobrenome": "White", 
    "idaide": 30,
    "ativo": False,
    "notas": ["A", "A+"],
    "telefones": {
        "residencial": "00 123456789",
        "celulcar": "01 234567890"
    }

},
    {"nome": "Valéria", 
    "sobrenome": "Cristina", 
    "idaide": 30,
    "ativo": True,
    "notas": ["B", "B+"],
    "telefones": {
        "residencial": "99 987654321",
        "celulcar": "98 0976544321"
    }
}
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, '77.salvando_em_json.json')

print('-----dump-----')
print('dump salva o arquivo, load carrega o arquivo')
with open(SAVE_TO, 'w') as file:
    # dump() grava os dados em um arquivo
    json.dump(pessoas, file, indent=2)


# dumps() os representa como um objeto byte.

#print('-----dumps-----')
# print(json.dumps(pessoas, indent= 2))

JSON_FILE= os.path.join(BASE_DIR, '77.salvando_em_json.json')

print('-----load-----')
with open(JSON_FILE, 'r') as file:
    # load() lê objetos em conserva de um arquivo
    pessoas = json.load(file)
    
    for pessoa in pessoas:
        print(pessoa['nome'])

print('-----loads-----')
# loads() os desserializa 
# (Converte uma série de bits isolados num 
# fluxo paralelo com as mesmas informações)
json_string = '''
    [{"nome": "Alexandre", "sobrenome": "White", "idade": 30, "ativo": false, "notas": ["A", "A+"], "telefones": {"residencial": "00 123456789", "celulcar": "01 234567890"}}, {"nome": "Val\u00e9ria", "sobrenome": "Cristina", "idaide": 30, "ativo": true, "notas": ["B", "B+"], "telefones": {"residencial": "99 987654321", "celulcar": "98 0976544321"}}]'''

pessoas = json.loads(json_string)

for pessoa in pessoas:
    print(pessoa['nome'])