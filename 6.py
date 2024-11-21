globalList = [27, 3, 30, 2, 19, 2, 26, 3, 27, 3, 27, 2, 27, 10, 2]

def aTask():
    aList = [27, 3, 26, 8, 25, 7, 26, 3, 27, 3, 27, 2, 27, 27, 3]
    maxCount = 0

    for i in range(len(aList) - 1):
        if (aList[i] == max(aList)):
            maxCount += 1
    
    print(f"{maxCount} alkalommal.") # A leírásban 3 van viszont 5 van benne.

def bTask():
    print(f"A terjedelme {max(globalList) - min(globalList)} volt.") # A leírásban 20 van benne viszont a legnagyobb érték 30 a legkisebb 2 tehát 28...

def cTask():
    avarage = sum(globalList) / len(globalList)
    higherThanAvarage = 0
    lowerThanAvarage = 0

    for i in range(len(globalList)):
        if (globalList[i] > avarage):
            higherThanAvarage += 1
        else:
            lowerThanAvarage += 1

    if (higherThanAvarage > lowerThanAvarage):
        print(f"Az átlagnál nagyobb elemekből van több.")
    elif (higherThanAvarage < lowerThanAvarage):
        print(f"Az átlagnál kisebb elemekből van több.")
    else:
        print("Egyenlő")

    #átlag = 13.8

    #27 = NAGYOBB
    #3 = KISEBB
    #30 = NAGYOBB
    #2 = KISEBB
    #19 = NAGYOBB
    #2 = KISEBB
    #26 = NAGYOBB
    #3 = KISEBB
    #27 = NAGYOBB
    #3 = KISEBB
    #27 = NAGYOBB
    #2 = KISEBB
    #27 = NAGYOBB
    #10 = KISEBB
    #2 = KISEBB

    #NAGYOBB = 7
    #KISEBB = 8

    # A feladatban ÁLLÍTÓLAG a nagyobból van több. De látható, hogy nem.

def dTask():
    isWinterMonth = False

    for i in range(len(globalList)):
        if (globalList[i] < 0):
            isWinterMonth = True

    print("Nem téli hónap" if not isWinterMonth else "Téli hónap")


aTask()
bTask()
cTask()
dTask()