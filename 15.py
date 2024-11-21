import math

globalList = [100, 110, 200, 150, 300, 180, 150, 150, 100, 100]

def aTask():
    sumOfList = sum(globalList)

    print(f"{sumOfList} mp = {(sumOfList % 3600) // 60} perc és {sumOfList % 60} másodperc")


def bTask():
    k = int(input())
    position = 0

    for i in range(len(globalList) - 1):
        if (globalList[i] > k):
            position = i

    print(f"Igen volt, méghozzá a(z) {position + 1}. zeneszám.")

def cTask():
    # Első 4 számot összeadjuk, kivonjuk az 5-iket és 6-ikat

    sumOfTheFirstFour = sum(globalList[:4])
    sumOfList = sum(globalList)    
    leftSeconds = sumOfList + (sumOfTheFirstFour - (globalList[4] + globalList[5]))

    print(f"{leftSeconds} = {(leftSeconds % 3600) // 60} perc")

def dTask():
    # 1 kör = 180 mp
    k = int(input())
    kSeconds = sum(globalList[:k - 1])

    print(f"A {math.floor(kSeconds / 180)}. körünket futjuk.")

aTask()
bTask()
cTask()
dTask()