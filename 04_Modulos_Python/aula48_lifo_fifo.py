# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue

# Lifo é uma pilha (stack)
# Fifo é uma fila (queue)

# LIFO - (Last in first out)
# Pilha - (Stack)
# Significa que o último item a entrar será o primeiro a sair (list)

# vídeo: https://www.youtube.com/watch?v=svWVHEihyNI
# Para tirar/adicionar itens do final: O(1) Tempo Constante
# Para tirar/adicionar itens do início: O(n) Tempo Linear

from collections import deque

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅LEGAL LIFO com lista
#  0  1  2  3  4  5  6  7  8  9, 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista.append(10)
#  0  1  2  3  4  5  6  7  8  9, 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista.append(11)
#  0  1  2  3  4  5  6  7  8  9, 10, 11
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

ultimo_removido = lista.pop()
#  0  1  2  3  4  5  6  7  8  9 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Último: ', ultimo_removido)
print('Lista: ', lista)

#  0  1  2  3  4  5  6  7  8  9 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print()

# 🚫RUIM FIFO - (First in first out)
# 0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.insert(0, 10)
# 0  1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.insert(0, 11)
#   0   1  2  3  4  5  6  7  8  9 10 11
# [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

primeiro_removido = lista.pop()
#   0   1  2  3  4  5  6  7  8  9 10 11
# [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Primeiro: ', primeiro_removido) # 11
print('Lista: ', lista) # [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print()

# FIFO (First In First Out)
# Filas (queue)
# Significa que o primeiro item a entrar será o primeiro a sair (deque)
# Artigo:
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Vídeo:
# https://youtu.be/RHb-8hXs3HE
# Para tirar/adicionar itens do final: O(1) Tempo constante
# Para tirar/adicionar itens do início: O(1) Tempo constante

# ✅Legal (FIFO com deque)

fila_correta: deque[int] = deque()  # Deque vem zerado por padrão
fila_correta.append(3)  # Adiciona no final
fila_correta.append(4)  # Adiciona no final
fila_correta.append(5)  # Adiciona no final
fila_correta.appendleft(2)  # Adiciona no começo
fila_correta.appendleft(1)  # Adiciona no começo
fila_correta.appendleft(0)  # Adiciona no começo
print(fila_correta)  # deque([0, 1, 2, 3, 4, 5])
fila_correta.pop()  # 5
fila_correta.popleft()  # 0
print(fila_correta)  # deque([1, 2, 3, 4])