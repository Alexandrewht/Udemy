# threads
# https://docs.python.org/3/library/threading.html
from time import sleep
from threading import Thread
from threading import Lock

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            return
        
        sleep(1) # Cuidado com o sleep em threads, pois pode causar conflitos

        print(f'Você comprou, {quantidade} ingresso(s).'
              f' Ainda temos {self.estoque} em estoque.')
        self.estoque -= quantidade

        self.lock.release()
        

if __name__ == '__main__':
    ingressos = Ingressos(10)

    '''ingressos.comprar(1)
    ingressos.comprar(1)
    ingressos.comprar(1)
    ingressos.comprar(1)'''

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i, ))
        t.start()