#08_FenyjatekTombbel.py
#---------------------------
#Fényjáték bit-minta tömbbel

import RPi.GPIO as GPIO
import time
import random
import os.path
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#pin változók
pRed1 = 37
pYellow1 = 35
pGreen1 = 33
pRed2 = 40
pYellow2 = 38
pGreen2 = 36

T = 1.0
k = 2
T = T/k
n = 10 #ismétlések száma

#Fény bit-minta szalag
patternRibbon =[
                    [1,0,0,0,0,0],
                    [0,1,0,0,0,0],
                    [0,0,1,0,0,0],
                    [0,0,0,1,0,0],
                    [0,0,0,0,1,0],
                    [0,0,0,0,0,1],
                ]


#A lábak definiálása: mindegyik kimenet lesz
pins = [pRed1, pYellow1, pGreen1, pRed2, pYellow2, pGreen2]
#minden pin legyen kimenet
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#Led kigyújtó minta szerint
def LedFromPattern(pattern):
    print(pattern)
    for i in range(0, len(pattern)):
        GPIO.output(pins[i], pattern[i])

#Fény bit-minta tömb lejátszó függvény
def LedFromPatternRibbon(patternRibbon, n):
    for i in range(n):
        for pattern in patternRibbon:
            LedFromPattern(pattern)
            time.sleep(T)
   
try:
    LedFromPatternRibbon(patternRibbon, n)
    GPIO.cleanup()
    print("Vége. Pinek kikapcsolva")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Folyamat megszakítva, Pinek kikapcsolva")

