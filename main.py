import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+5585999053389']

while len(contatos) >= 1:

    pywhatkit.sendwhatmsg(contatos[0],'Deixa para a proxima',datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('crtl + w')