import math

globalList = [2, 1, 2, 3, 5, 12, 6, 6, 4, 3]

def aTask():
    aList = [2, 1, 2, 3, 5, 7, 6, 6, 4, 3]
    biggerThanFive = 0

    for i in aList:
        if (i < 5):
            biggerThanFive += 1
    
    print(f"{biggerThanFive} napon mértünk maximum 5 fokot")

def bTask():
    biggestDifference = 0
    pos1 = 0
    pos2 = 0
    
    for i in range(len(globalList) - 1):
        if ((globalList[i + 1] - globalList[i] >= biggestDifference)):

            biggestDifference = abs(globalList[i + 1] - globalList[i])
            pos1 = i + 1
            pos2 = i + 2

    print(f"{pos1}. és {pos2}. nap között volt a legnagyobb hőingadozás: {biggestDifference}.")

def cTask():
    print(f"A terjedelme {max(globalList) - min(globalList)} volt.")

def dTask():
    average = sum(globalList) / len(globalList)
    squaredDifference = 0

    for i in globalList:
        squaredDifference += (i - average) ** 2
    
    print(f"Minta szórása: {math.sqrt(squaredDifference / (len(globalList) - 1)):.3f}")


aTask()
bTask()
cTask()
dTask()
