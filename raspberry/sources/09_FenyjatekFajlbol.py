#09_FenyjatekFajlbol.py
#---------------------------
#Fényjáték bit-minta fájlból

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
k = 10
T = T/k
n = 10 #ismétlések száma


#mintaSzalag beolvasás fájlból
def patternRibbonFromFile(file):
    patternRibbon = []
    if os.path.exists(file):
        #sorok tömbbe olvasása: ahány sor annyi elem
        f = open(file, "r")
        rows = f.readlines()
        #sorok tömbbé alakítása
        for row in rows:
            #sorvége karakterek levágása
            row = row.rstrip()
            #egy sor tömbbé alakítása
            pattern = list(row)           
            #sortömb hozzáadása az patternRibbon tömbhöz    
            patternRibbon.append(pattern)
    else:
        print("{0} fájl nem létezik!".format(file))
        raise KeyboardInterrupt
    return patternRibbon

file = "minta1.txt"

#Fény minta szalag
patternRibbon = patternRibbonFromFile(file)


#A lábak definiálása: mindegyik kimenet lesz
pins = [pRed1, pYellow1, pGreen1, pRed2, pYellow2, pGreen2]
#minden pin legyen kimenet
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#Led kigyújtó minta szerint
def LedFromPattern(pattern):
    print(pattern)
    for i in range(0, len(pattern)):
        GPIO.output(pins[i], int(pattern[i]))

#Minta tömb lejátszó
def LedFromPatternRibbon(patternRibbon, n):
    for i in range(n):
        for pattern in patternRibbon:
            LedFromPattern(pattern)
            time.sleep(T)
   
try:
    file = raw_input("Adja meg a minta fájlt: ")
    patternRibbon = patternRibbonFromFile(file)
    LedFromPatternRibbon(patternRibbon, n)
    GPIO.cleanup()
    print("Vége. Pinek kikapcsolva")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Folyamat megszakítva, Pinek kikapcsolva")

