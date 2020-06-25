#05_LedVillogMindFuggveny.py
#------------------------------
#Ledek villogtatása függvénnyel

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
#Pinek definiálása
pins = [37,35,33,40,38,36]
T = 0.5 #Villogás periódusideje
Tv = T/2
onOff = 1 #Led bekapcsolása

#Függvények
#A pinek legyenek kimenetek
def DefPinsOut():
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def LampBlink():
    global onOff #Az onOff globális változó
    for pin in pins:
        GPIO.output(pin, onOff)
    onOff = not onOff #Nem jön létre új változó

#A Pinek kimenetek
#Függvény hívás
DefPinsOut()        

print("Pinek villognak. Kilép Ctrl-C")
try:
    while True:
        LampBlink()
        time.sleep(Tv)

except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()
