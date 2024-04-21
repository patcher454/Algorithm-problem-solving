from sys import stdin

N, M = map(int, stdin.readline().split())

numDict = {}
nameDict = {}
for i in range(1, N + 1):
    name = stdin.readline().replace('\n', '')
    numDict[i] = name
    nameDict[name] = i
    

for i in range(M):
    input = stdin.readline().replace('\n', '')
    if input.isdigit():
        print(numDict[int(input)])
        continue

    print(nameDict[input])
