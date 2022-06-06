##############################################################################################################
#
#
#
#
##############################################################################################################
##  Importation des librairies                                                                              ##
##############################################################################################################
#
#
#
##############################################################################################################
from machine import ADC
from machine import SoftI2C
from machine import Pin, PWM
import random
import _thread
import tm1637 
import usocket as socket
import uselect as select
import time
import onewire
import re
import gc


##############################################################################################################
##  Définition des capteurs et initialisation des valeurs                                                   ##
##############################################################################################################
#
#
##############################################################################################################
#...TM1637           | écran 7-Segment à 4 Chiffres 
tm= tm1637.TM1637(clk=Pin(15), dio=Pin(4))
tm.show('    ')
     # tm.show('10') #display the number 10 on the display

##############################################################################################################
#...                 | Module numérique de capteur d'intensité lumineuse
bouton= Pin(16, Pin.IN, Pin.PULL_DOWN)
     # bouton.value() # 1 si bouton, 0 sinon.

##############################################################################################################
#...KY-038           | Capteur de Son 
son_analog= ADC(Pin(36))
son_analog.atten(ADC.ATTN_11DB)       # Full range: 3.3v
son_analog.width(ADC.WIDTH_9BIT)     # Range 0 to 4095
son_digit= Pin(0, Pin.IN, Pin.PULL_DOWN)
     # son_analog.read()
     # son_digit.value() # 1 si son, 0 sinon.



##############################################################################################################
##  Boucle pincipale                                                                                        ##
##############################################################################################################
#
#
##############################################################################################################
temps = 0
blinker = True
while True :
  if son_digit.value() == 1:
    temps += 1
    minute  = int(temps / 60)
    seconde = int(temps % 60)
    tm.numbers(minute,seconde, blinker)
    time.sleep(0.5)
    blinker = not blinker
    tm.numbers(minute,seconde, blinker)
    time.sleep(0.5)
    blinker = not blinker
