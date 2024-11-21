globalList = [185, 158, 159, 160, 167, 174, 172, 185]

def aTask():
    aList = [160, 185, 159, 185, 167, 174, 172, 185]
    found = False

    for i in range(len(aList) - 1):
        if ((i != 0) and (i != len(aList))):
            if ((aList[i + 1] >= aList[i]) and (aList[i - 1] >= aList[i]) and (not found)):
                found = True
                print(f"A(z) {i + 1}. diák csak a mellette lévőket látja.")

def bTask():
    # Akkor jó ha a i - 1 < i ÉS i + 1 > i
    wrongCount = 0
    
    for i in range(len(globalList) - 1):
        if ((i != 0) and (i != len(globalList))):
            if (globalList[i + 1] < globalList[i] or globalList[i - 1] > globalList[i]):
                wrongCount += 1
    
    print(f"{wrongCount} db rossz helyen álló diák van.")

def cTask():
    # 1360 / 8 = 170
    higherThanAvarage = 0
    lowerThanAvarage = 0
    avarage = sum(globalList) / len(globalList)

    print(avarage)

    for i in range(len(globalList)):
        if (globalList[i] > avarage):
            higherThanAvarage += 1
        else:
            lowerThanAvarage += 1
        
    if (higherThanAvarage == lowerThanAvarage):
        print("Egyenlő")
    elif (higherThanAvarage > lowerThanAvarage):
        print("A magassabból volt több.")
    else:
        print("Az alacsonyabból volt több.")

def dTask():
    dList = [185, 175, 182, 159, 167, 174, 172, 185]
    maxLength = 0
    startIndex = -1
    currentStart = 0
    
    for i in range(1, len(dList)):
        if (dList[i] > dList[i - 1]):
            currentLength = i - currentStart + 1

            if (currentLength > maxLength):
                maxLength = currentLength
                startIndex = currentStart
        else:
            currentStart = i
    
    print(f"{startIndex + 1} a {startIndex + maxLength}. gyerektől")



aTask()
bTask()
cTask()
dTask()