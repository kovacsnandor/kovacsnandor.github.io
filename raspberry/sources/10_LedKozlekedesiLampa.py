#10_LedKozlekedesiLampa.py
#-------------------------
#Közlekedési lámpa

#Alapbeállítások
import RPi.GPIO as GPIO
import time
#GPIO beállítások
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

pRedVehicle = 40
pGreenVehicle = 38
pYellowVehicle = 36
pRedPedestrian = 37
pGreenPedestrian = 33
#pinek tömbje
pins = [
    pRedVehicle,
    pGreenVehicle,
    pYellowVehicle,
    pRedPedestrian,
    pGreenPedestrian
    ]
#ciklussal ezek a pinek kimenetek lesznek
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#Jármű lámpa gyújtogató
def LampVehicle(r, y, g):
    GPIO.output(pRedVehicle, r)
    GPIO.output(pGreenVehicle, y)
    GPIO.output(pYellowVehicle, g)

#Gyalogos lámpa gyújtogató
def LampPedestrian(r, g):
    GPIO.output(pRedPedestrian, r)
    GPIO.output(pGreenPedestrian, g)

#lámpa teszt függvény
#n: hányszor villan    
def Test(n):
    print("Teszt...")
    onOff = 1
    for i in range(n):
        LampVehicle(onOff, onOff, onOff)
        LampPedestrian(onOff, onOff)
        onOff = not onOff
        time.sleep(0.5)
    time.sleep(0.5)
    onOffeg = 0
    LampVehicle(onOff, onOff, onOff)
    LampPedestrian(onOff, onOff)
    print("Teszt vége")


#A program paraméterezése
T = 1.0 #órajel periódusidő: 1s
k = 5 #Idő gyorsítás: pl. 5: 5-ször gyorsabb
Treal = T/k #tényleges órajel

f = (1/Treal)*2 #a gyalogos zöld villogási frekvenciája
t = 0 #Ezzel mérem az időt 
#A lámpa idők definiálása
tRed = 10 #Eddig ég a piros
tYellowRed = 3 #Eddig ég a Sárga és piros
tGreen = 10 #Zöld
tYellow = 3 #Sárga
tSum = tRed + tYellowRed + tGreen + tYellow #összidő

try:
    #indítjuk a tesztet
    Test(5)

    print("Közelekedési lámpák. Gyorsítás: {0} Kilép: Ctrl-C".format(k))

    
    while True:
        if t == tSum:
            t = 0
            
        if t == 0:
            #jármű:piros, gyalogos: zöld
            LampVehicle(1, 0, 0)
            LampPedestrian(0,1)
        
        if t == tRed:
            #jármű: piros-sárga: gyalogos: villogó zöld
            LampVehicle(1,1,0)
            #villogás
            p = GPIO.PWM(pGreenPedestrian, f)
            p.start(50)
             
        if t == tRed + tYellowRed:
            #jármű: zöld: gyalogos: villogás stop, piros          
            LampVehicle(0,0,1)
            p.stop()
            LampPedestrian(1,0)
         
        if t ==  tRed + tYellowRed + tGreen:
            #jármű: sárga: gyalogos: piros 
            LampVehicle(0,1,0)
            LampPedestrian(1,0)
            
        #print(t)    
        t += 1
        time.sleep(Treal)
        
except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()



