import sys
import time

from worker import Ui_myWidget
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal, QThread

class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def doWork(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)

        self.finished.emit(value)

class Worker2(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def executeMe(self):
        value = '0'
        self.started.emit(value)
        for i in range(50, 100, 5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(0.3)

        self.finished.emit(value)

class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker1 = Worker1()
        self._thread1 = QThread()

        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker1
        thread = self._thread1

        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto ed worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # QUando uma QThread é iniciada, emite o sinal started automaticamente.
        thread.started.connect(worker.doWork)

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da QThread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        # deletelLater solicita a exclusão do objeto worker do sistema de gerenciamento
        # de memória do Python. Quando o worker finaliza, ele emite um sinal finished que
        # vai executar o método deleteLater. Isso garante que os objetos sejam
        # removidos da memória corretamente.
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        # Aqui todos seus métodos e início, meio e fim são executados na thread
        # execute o que quiser
        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        # Inicie a thread
        thread.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('1 iniciado')

    def worker1Progressed(self, value):
        self.label1.setText(value)
        print('1 em progresso')

    def worker1Finished(self, value):
        self.button1.setDisabled(False)
        self.label1.setText(value)
        print('1 finalizado')

    def hardWork2(self):
        self.label2.setText('OK')

    
    def hardWork2(self):
        self._worker2 = Worker2()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Conectar os sinais do worker para a thread
        thread.started.connect(worker.executeMe)
        worker.finished.connect(thread.quit)

        # Deletar os sinais finalizados da memória
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        thread.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('2 iniciado')

    def worker2Progressed(self, value):
        self.label2.setText(value)
        print('2 em progresso')

    def worker2Finished(self, value):
        self.button2.setDisabled(False)
        self.label2.setText(value)
        print('2 finalizado')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec()