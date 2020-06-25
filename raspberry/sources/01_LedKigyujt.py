#01_LedKigyujt.py
#--------------------------
#Led kigyújtása változókkal

#A GPIO modul behívása
import RPi.GPIO as GPIO
import time

#Figyelmezetetések kikapcsolása
GPIO.setwarnings(False)

#tüskék fizikai kiosztás szerint
GPIO.setmode(GPIO.BOARD)

#tüskék alaphelyzet
GPIO.cleanup()

#A program paraméterei:
#Pin definiálása
pin = 36
onOff = 1

#A "pin" tüske kimenet
GPIO.setup(pin, GPIO.OUT)

#Led kigyújt
GPIO.output(pin, onOff)


print("Pin_%s világít. Kilép Ctrl-C" %(pin))
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()
