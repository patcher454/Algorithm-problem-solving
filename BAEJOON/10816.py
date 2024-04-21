from sys import stdin

stdin.readline()
countDict = {}
for i in map(int, stdin.readline().split()):
    if i not in countDict:
        countDict[i] = 1
        continue
    countDict[i] = countDict[i] + 1
    
    
stdin.readline()
for i in map(int, stdin.readline().split()):
    if i not in countDict:
        print(0, end = " ")
        continue
    print(countDict[i], end = " ")