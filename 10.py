import math

numbersList = [90, 160, 170, 350, 550, 550, 890, 1000, 1100]

def aTask():
    currentHighland = 0

    for i in range(len(numbersList) - 1):
        if (numbersList[i] > 220) and (numbersList[i] == numbersList[i + 1]): # Ha az adott elem 220 fölött van és egyezik a következő elemmel
            currentHighland += numbersList[i] # hozzáadjuk a fennsík változóhoz

    print(f"Az {numbersList.index(currentHighland) + 1}. mérési ponton már fennsíkon vagyunk.")

def bTask():
    possibleAngles = []
    found = False

    for i in range(len(numbersList) - 1):
        if (numbersList[i + 1] - numbersList[i] != 0): # Ha az elem + 1 - elem NEM nulla 
            possibleAngles.append(numbersList[i + 1] - numbersList[i]) # Hozzáadjuk a lehetséges szögek listájához
    
    for i in range(len(numbersList) - 1):
        if (numbersList[i + 1] - numbersList[i] == min(possibleAngles)) and (not found): # Ha a globális lista elem + 1 - elem egyenlő a legkisebb elemmel ÉS még nincsen meg
            smallestAnglePosition = i # Beállítjuk a pozicíot
            found = True # Kikapcsoljuk
    
    print(f"Az {smallestAnglePosition}. mérési ponton volt a legkisebb emelkedési szög.")

def cTask():
    angles = []
    
    for i in range(len(numbersList) - 1):
        angles.append(math.atan(numbersList[i + 1] - numbersList[i])) # Hozzádjuk a tömbhöz a különbség ARCTAN-ját
    
    if (angles): # Ha nem üres a tömb akkor kiírjuk
        print(f"{sum(angles) / len(angles):.3f}")

def dTask():
    isContinuous = False

    if (sorted(numbersList) == numbersList): # Ha a szortírozott lista egyenlő a globális listával 
        isContinuous = True
    else:
        isContinuous = False
    
    print(f"Folyamatos" if isContinuous else f"Nem folyamatos")

aTask()
bTask()
cTask()
dTask()