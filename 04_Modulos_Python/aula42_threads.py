# threads
# https://docs.python.org/3/library/threading.html
from time import sleep
from threading import Thread

'''print('Hello World')

for i in range(10):
    print(i)
    sleep(.5)

print('World!')'''

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

for i in range(10):
    print(i)
    sleep(1)

'''
as threads estão sendo executadas em paralelo
0
1
Thread 3
2
Thread 2
3
4
Thread 1
5
6
'''