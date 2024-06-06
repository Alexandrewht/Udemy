#"format" é um método que permite formatar strings 
# de forma mais flexível e dinâmica. 
# Ele é usado para inserir valores em uma string formatada, 
# também conhecida como "string de formatação".

a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}' # mesmo sem declarar variável é possível usar o format
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)