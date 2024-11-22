abList = [2, 0, 3, 1, 1, 3, 1, 2, 1, 1, 1, 3]

def aTask():
    kszWinCount = 0
    kblWinCount = 0
    kblMatches = abList[::2]
    kszMatches = abList[1::2]

    for i in range(len(kblMatches)):
        if (kblMatches[i] > kszMatches[i]):
            kblWinCount += 1
        elif (kblMatches[i] < kszMatches[i]):
            kszWinCount += 1
    
    if (kszWinCount > kblWinCount):
        print("A KSZ csapat nyert többször")
    elif (kszWinCount < kblWinCount):
        print("A KBL csapat nyert többször")
    else:
        print("Egyenlő")

def bTask():
    kblMatches = abList[::2]
    kszMatches = abList[1::2]
    isThereEqual = False

    for i in range(len(kblMatches)):
        if (kblMatches[i] == kszMatches[i]):
            isThereEqual = True
    
    print("Igen volt ilyen" if isThereEqual else "Nem volt ilyen")

def cTask():
    kblMatches = abList[::2]
    kszMatches = abList[1::2]
    zeroCount = 0

    for i in range(len(kblMatches)):
        if ((kblMatches[i] == 0) and (kszMatches[i] == 0)):
            zeroCount += 1
    
    print(f"{zeroCount} alkalommal volt 0-0 az állás.")

aTask()
bTask()
cTask()