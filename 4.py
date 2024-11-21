def aTask():
    aList = [101, 138, 112, 121, 176, 163, 123, 210, 226]
    sillCount = 0
    maxHeight = aList[0]

    for i in range(1, len(aList)):
        if (aList[i] > maxHeight):
            sillCount += 1
            maxHeight = aList[i]

    print(f"(1.) {sillCount} küszöb van.")

def bTask():
    bList = [101, 138, 112, 121, 176, 163, 123, 226, 210]
    mountainPeakCount = 0

    for i in range(len(bList) - 1):
        if (bList[i] > bList[i - 1] and bList[i] > bList[i + 1]):
            mountainPeakCount += 1

    print(f"(2.) Összesen {mountainPeakCount} hegycsúcs.")

def cTask():
    cList = [101, 138, 112, 112, 176, 163, 123, 226, 210]
    found = False
    position = 0

    for i in range(len(cList) - 1):
        if (cList[i] == cList[i + 1] and (not found)):
            position = i
            found = True

    print(f"(3.) {position + 1} mérés ponton nyereg van!")

def dTask():
    dList = [101, 138, 112, 112, 176, 163, 123, 226, 210]
    calculatedDifferences = []
    
    for i in range(len(dList) - 1):
        if (dList[i + 1] - dList[i] != 0):
            calculatedDifferences.append(dList[i + 1] - dList[i])
    
    print(f"(4.) {max(calculatedDifferences)} m volt a legnagyobb szintkülönbség.")


aTask()
bTask()
cTask()
dTask()