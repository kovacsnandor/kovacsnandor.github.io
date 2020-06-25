#02_LedVillog.py
#-------------------------
#Led villogtatás ciklussal

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
pin = 36 #Pin definiálása
T = 0.1 #Villogás periódusideje
Tv = T/2
onOff = 1

#A "pin" tüske kimenet
GPIO.setup(pin, GPIO.OUT)

print("Pin_%s villog. Kilép Ctrl-C" %(pin))
try:
    while True:
        GPIO.output(pin, onOff)
        onOff = not onOff
        time.sleep(Tv)

except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()
