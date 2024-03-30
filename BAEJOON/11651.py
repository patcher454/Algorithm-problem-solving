from sys import stdin
dict = {}
for i in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    if y not in dict:
        dict[y] = []
    dict[y].append(x)
    
for i in sorted(dict):
    for item in sorted(dict[i]):
        print(str(item) + " " + str(i))