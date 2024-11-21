globalList = [0, 500, 100, 700, 350, 650, 20, 550, 10, 0]

def aTask():
    found = False
    valleys = []

    for i in range(len(globalList) - 1):
        if ((globalList[i] < globalList[i - 1]) and (globalList[i] < globalList[i + 1])):
            valleys.append(globalList[i])

    for i in range(len(globalList)):
        if ((globalList[i] == max(valleys)) and (not found)):
            found = True
            print(f"Legmagasabb völgy: {i + 1} mérésnél.")

def bTask():
    # Akkor van hegycsúcs ha az i körül lévő 2 adat kisebb mint i
    mountainPeaks = []
    found = False

    for i in range(len(globalList)):
        if ((globalList[i] > globalList[i - 1]) and (globalList[i] > globalList[i + 1])):
            mountainPeaks.append(globalList[i])

    for i in range(len(globalList)):
        if ((globalList[i] == min(mountainPeaks)) and (not found)):
            found = True
            print(f"Legalacsonyabb hegycsúcs a {i + 1}. mérési pontnál volt {min(mountainPeaks)}m")

def cTask():
    biggerThanDifferenceCount = 0
    difference = int(input())

    for i in range(len(globalList) - 1):
        if (globalList[i + 1] - globalList[i] >= difference):
            biggerThanDifferenceCount += 1

    print(f"{biggerThanDifferenceCount} alkalommal fordul elő, hogy a szintkülönbség több a bekért adatnál.")


def dTask():
    descendingCount = 0

    for i in range(len(globalList) - 1):
        if (globalList[i] > globalList[i + 1]):
            descendingCount += 1
        else:
            descendingCount = 0
    
    print(f"A leghosszabb sorozat, amikor lejtőn vagyunk: {descendingCount + 1}.")



aTask()
bTask()
cTask()
dTask()