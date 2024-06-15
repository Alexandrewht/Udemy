'''# script para trapacear
import pyautogui
import keyboard
import time

# Função para verificar se a tecla "Esc" foi pressionada
def check_esc():
    return keyboard.is_pressed('esc')

# Loop principal
while True:
    if check_esc():
        print("Programa encerrado.")
        break

    # Capturar as coordenadas do cursor
    x, y = pyautogui.position()

    # Capturar a cor do pixel sob o cursor
    cor_pixel = pyautogui.screenshot().getpixel((x, y))

    # Se a cor for amarela (R, G, B = 255, 255, 0), clique
    if cor_pixel == (255, 255, 0):
        pyautogui.click(x, y)
        print("Cliquei em um pixel amarelo!")
        #time.sleep(1)  # 1 segundo 
        #time.sleep(0.04)  # 4 milisegundos 
        time.sleep(0.01)  # 10 milisegundos 
'''
# rng de cores.
import random

# Função para gerar uma cor RGB aleatória
def cor_aleatoria():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Exemplo de uso
cor = cor_aleatoria()
print("Cor aleatória:", cor)