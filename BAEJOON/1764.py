from sys import stdin

n, m = map(int, stdin.readline().split())

liSet = set()
for i in range(n):
    liSet.add(stdin.readline())
    
loSet = set()
for i in range(m):
    loSet.add(stdin.readline())
    
result = liSet & loSet
print(len(result))
for item in sorted(result):
    print(item.replace("\n", ""))
