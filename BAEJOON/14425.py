from sys import stdin

n, m = map(int,stdin.readline().split())
stringSet = set([])
for i in range(n):
    stringSet.add(stdin.readline())
    
count = 0
for i in range(m):
    if stdin.readline() in stringSet:
        count += 1
        
print(count)
