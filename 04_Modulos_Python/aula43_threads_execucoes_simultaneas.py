# threads
# https://docs.python.org/3/library/threading.html
from time import sleep
from threading import Thread


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()

'''t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 2))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 1))
t3.start()

for i in range(10):
    print(i)
    sleep(.5)'''

while t1.is_alive():
    print('Esperando a thread terminar...')
    sleep(2)

print('Thread terminada!')