#07_FenyjatekMintaval.py
#---------------------------
#Fényjáték bit-minta alapján

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

T = 1.0 #alap bit-minta idő (1s)
k = 10 #gyorsítási tényező
T = T/k #periódusidő k-szorosára gyorsítása
n = 10 #ismétlések száma

#Fény bit-minta tömbök
pattern1 = [0,1,0,1,0,1]
pattern2 = [1,0,1,0,1,0]


#A lábak definiálása: mindegyik kimenet lesz
pins = [pRed1, pYellow1, pGreen1, pRed2, pYellow2, pGreen2]
#minden pin legyen kimenet
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#Led kigyújtó függvény bit-minta szerint
def LedFromPattern(pattern):
    print(pattern)
    for i in range(0, len(pattern)):
        GPIO.output(pins[i], pattern[i])

try:
    for i in range(n):
        LedFromPattern(pattern1)
        time.sleep(T)
        LedFromPattern(pattern2)
        time.sleep(T)
        
    GPIO.cleanup()
    print("Vége. Pinek kikapcsolva")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Folyamat megszakítva, Pinek kikapcsolva")

