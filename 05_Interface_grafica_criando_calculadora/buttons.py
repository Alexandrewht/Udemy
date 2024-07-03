from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MID_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    # Cuidado ao sobre escrever os estilos
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MID_FONT_SIZE)
        # font.setBold(True)
        # font.setItalic(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        # self.setCheckable(True)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        # grid com as teclas numéricas e operadores matematicos
        self._gridMask = [
            ['C', '←', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            j = 0
            while j < len(row):
                buttonText = row[j]
                if buttonText == '':
                    j += 1
                    continue
                
                if buttonText == '0':
                    button = Button(buttonText)
                    self.addWidget(button, i, j, 1, 2)
                    j += 2
                else:
                    button = Button(buttonText)
                    if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                        button.setProperty('cssClass', 'specialButton')
                        self._configSpecialButton(button)
                    self.addWidget(button, i, j)
                    j += 1

                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        
        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '←':
            self._connectButtonClicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._operatorClicked, button)
            )

        if text in '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)
               
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()  # +-/* (etc...)
        displayText = self.display.text()  # número da esquerda _left
        self.display.clear()  # limpa o display após clicar em um operador

        # se a pessoa clicou no operador sem configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada')
            return
        
        # se houver um número da esquerda, não fazemos nada
        # aguardaremos o número da direita 
        if self._left is None:
            self._left = float(displayText)

        # se selecionar o número da esquerda, e selecionar um operador,
        # e se arrepender e querer mudar o operador, pode mudar o operador
        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('Conta incompleta')
            return
        
        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        # CUIDADO COM EVAL: https://docs.python.org/3/library/functions.html#eval
        # EVAL Executa o código passando a ele uma string, se a entrada para o eval
        # for derivada de dados não confiável, isso pode permitir ataques de injeção
        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Essa conta não pode ser realizada')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self._left = None

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()

        # # Apenas demonstração do que é possível fazer com o msgBox
        # msgBox.setInformativeText('Deseja continuar?')
        # msgBox.setStandardButtons(msgBox.StandardButton.Ok |
        #                            msgBox.StandardButton.Cancel |
        #                            msgBox.StandardButton.Save
        #                            )
        # # msgBox.button(msgBox.StandardButton.Cancel).setText('Cancelar')

        # result = msgBox.exec()

        # if result == msgBox.StandardButton.Ok:
        #     print('usuário clicou em Ok')
        # elif result == msgBox.StandardButton.Cancel:
        #     print('usuário clicou em Cancel')
        # elif result == msgBox.StandardButton.Save:
        #     print('usuário clicou em Save')

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()