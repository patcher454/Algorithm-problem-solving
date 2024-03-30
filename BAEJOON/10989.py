from sys import stdin
n = int(stdin.readline())
counts = [0 for i in range(10000)]

for i in range(n):
    counts[int(stdin.readline()) - 1] += 1
    
for i in range(len(counts)):
    for j in range(counts[i]):
        print(i + 1)
