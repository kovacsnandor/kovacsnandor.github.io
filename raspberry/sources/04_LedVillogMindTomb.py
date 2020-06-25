#04_LedVillogMindTomb.py
#-------------------------
#Ledek villognak ciklussal

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

#A Pinek kimenetek
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#Led bekapcsolása
onOff = 1

print("Pinek villognak. Kilép Ctrl-C")
try:
    while True:
        for pin in pins:
            GPIO.output(pin, onOff)
        onOff = not onOff
        time.sleep(Tv)

except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()
