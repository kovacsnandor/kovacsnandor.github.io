#03_LedVillogMind.py
#--------------------
#Mindegyik led villog

#A GPIO modul behívása
import RPi.GPIO as GPIO
import time

#Figyelmezetetések kikapcsolása
GPIO.setwarnings(False)

#tüskék fizikai kiosztás szerint
GPIO.setmode(GPIO.BOARD)

#tüskék alaphelyzet
GPIO.cleanup()

#Paraméterek
pin36 = 36 #Pinek definiálása
pin38 = 38
pin40 = 40
pin33 = 33
pin35 = 35
pin37 = 37
T = 0.1 #Villogás periódusideje
Tv = T/2 
onOff = 1 #Led bekapcsolása

#A Pinek kimenetek
GPIO.setup(pin36, GPIO.OUT)
GPIO.setup(pin38, GPIO.OUT)
GPIO.setup(pin40, GPIO.OUT)
GPIO.setup(pin33, GPIO.OUT)
GPIO.setup(pin35, GPIO.OUT)
GPIO.setup(pin37, GPIO.OUT)

print("Pinek villognak. Kilép Ctrl-C")
try:
    while True:
        GPIO.output(pin36, onOff)
        GPIO.output(pin38, onOff)
        GPIO.output(pin40, onOff)
        GPIO.output(pin33, onOff)
        GPIO.output(pin35, onOff)
        GPIO.output(pin37, onOff)
        onOff = not onOff
        time.sleep(Tv)

except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()
