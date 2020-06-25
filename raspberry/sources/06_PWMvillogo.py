#06_PWMvillogo.py
#----------------
#PWM villogó

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#36. tüske legyen kimenet
pin = 36
GPIO.setup(pin, GPIO.OUT)
frequency = 1
fill = 50
#A pin PWM üzemmódba kapcsolása
p = GPIO.PWM(pin, frequency)
#indítás
p.start(fill)
print("villogás: f={0} Hz kitöltés: {1} % Leállítás: Ctrl-C" .format(frequency, fill))

try:
    while True:
        cont = raw_input("Folytat? y/n: ")
        if cont == "n":
            p.stop()
            continue
        
        if cont == "y":
            p = GPIO.PWM(pin, frequency)
            p.start(fill)
            
        f = raw_input("f={0} Hz k: {1} % Írd be frekvenciát (1-1000): " .format(frequency, fill))
        k = raw_input("f={0} Hz k: {1} % Írd be kitötést (1-100): " .format(frequency, fill))
        print("------- Kilép: Ctrl-C ----------")
        if k.isdigit():
            fill = int(k)
            if fill in range(1,101):
                p.ChangeDutyCycle(fill)
                
        if f.isdigit():
            frequency = int(f)
            if frequency in range(1,1001):
                p.ChangeFrequency(frequency)     
        
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()


