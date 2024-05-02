from sys import stdin
from collections import deque

q = deque([])

n = int(stdin.readline())
for _ in range(n):
    command = stdin.readline().split()
    if len(command) == 2:
        q.append(int(command[1]))
        continue
    
    if command[0] == "pop":
        if len(q) <= 0:
            print(-1)
            continue
        print(q.popleft())
        continue
    
    if command[0] == "size":
        print(len(q))
        continue
    
    if command[0] == "empty":
        if len(q) == 0:
            print(1)
            continue
        print(0)
        continue
    
    if command[0] == "front":
        if len(q) <= 0:
            print(-1)
            continue
        print(q[0])
        continue
    
    if command[0] == "back":
        if len(q) <= 0:
            print(-1)
            continue
        print(q[-1])
        