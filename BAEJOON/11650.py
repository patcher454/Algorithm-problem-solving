from sys import stdin
dict = {}
for i in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    if x not in dict:
        dict[x] = []
    dict[x].append(y)
    
for i in sorted(dict):
    for item in sorted(dict[i]):
        print(str(i) + " " + str(item))