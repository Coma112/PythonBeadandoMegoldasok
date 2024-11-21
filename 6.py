globalList = [27.3, 30.2, 19.2, 26.3, 27.3, 27.2, 27, 10.2]

def aTask():
    aList = [27.3, 26.8, 25.7, 26.3, 27.3, 27.2, 27, 27.3]
    maxCount = 0

    for i in range(len(aList)):
        if (aList[i] == max(aList)):
            maxCount += 1
    
    print(f"{maxCount} alkalommal.")

def bTask():
    print(f"A terjedelme {round(max(globalList) - min(globalList))} volt.")

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