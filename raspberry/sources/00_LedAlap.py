#00_LedAlap.py
#-----------------
#Led gyújtása 0-ra

#A GPIO modul behívása
import RPi.GPIO as GPIO
#Az időzítő modul behívása
import time

#Figyelmezetetések kikapcsolása
GPIO.setwarnings(False)

#tüskék fizikai kiosztás szerint
GPIO.setmode(GPIO.BOARD)

#tüskék alaphelyzet
GPIO.cleanup()

#36-os tüske kimenet
GPIO.setup(36, GPIO.OUT)

#Led bekapcsolása
#GPIO.output(36, GPIO.HIGH)
GPIO.output(36, 1)
#GPIO.output(36, True)



print("Pin_36 világít. Kilép Ctrl-C")
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()
