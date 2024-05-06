from sys import stdin
from collections import deque

n = int(stdin.readline())
que = deque()
for _ in range(n):
    command = stdin.readline().split()
    if len(command) > 1:
        if int(command[0]) == 1:
            que.appendleft(int(command[1]))
            continue
        if int(command[0]) == 2:
            que.append(int(command[1]))
            continue
        
    if int(command[0]) == 3:
        if len(que) == 0:
            print(-1)
            continue
        
        print(que.popleft())
        continue
    if int(command[0]) == 4:
        if len(que) == 0:
            print(-1)
            continue
        
        print(que.pop())
        continue
    if int(command[0]) == 5:
        print(len(que))
        continue
    if int(command[0]) == 6:
        if len(que) == 0:
            print(1)
            continue
        print(0)
        continue
    if int(command[0]) == 7:
        if len(que) == 0:
            print(-1)
            continue
        
        print(que[0])
        continue
    if int(command[0]) == 8:
        if len(que) == 0:
            print(-1)
            continue
        
        print(que[-1])
        continue
    
