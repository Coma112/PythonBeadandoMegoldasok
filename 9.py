abList = [0, 10, 100, 700, 350, 0, 0, 0, 0, 20, 50, 10, 0]
cdList = [0, 10, 100, 100, 350, 0, 0, 0, 0, 20, 50, 10, 0]

def aTask():
    isIsland = False
    islandCount = 0

    for i in range(len(abList)):
        if (abList[i] > 0):
            if (not isIsland):
                isIsland = True
        elif (isIsland):
            islandCount += 1
            isIsland = False
    
    print(f"A szigetek száma: {islandCount}")


def bTask():
    maxWater = 0
    currentWater = 0
    isInWater = False

    for i in range(len(abList)):
        if (abList[i] == 0):
            if (isInWater):
                if (currentWater > maxWater):
                    maxWater = currentWater
                currentWater = 0 
                isInWater = False
        else:
            currentWater += 1
            isInWater = True

    if ((isInWater) and (currentWater > maxWater)):
        maxWater = currentWater

    print(f"A legnagyobb egybefüggő vízmennyiség {maxWater} mérési ponton keresztül volt.")

def cTask():
    isThereAvailableHighLand = False

    for i in range(len(cdList)):
        if (cdList[i] >= 200):
            isThereAvailableHighLand = True
    
    print("Igen található fennsík az adatok között" if isThereAvailableHighLand else "Nem található fennsík az adatok között")

def dTask():
    found = False

    for i in range(len(cdList)):
        if ((not found) and (cdList[i] == max(cdList))):
            found = True
            print(f"Az {i + 1}. mérési ponton lehet a legmesszebb látni.")
            

aTask()
bTask()
cTask()
dTask()