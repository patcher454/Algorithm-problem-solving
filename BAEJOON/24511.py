from collections import deque
n = int(input())
structure = list(map(int, input().split()))
queuestack = list(map(int, input().split()))
input()
data = list(map(int, input().split()))

que = deque([])
for i in range(len(structure)):
    if structure[i] == 0:
        que.appendleft(queuestack[i])

result = []
for item in data:
    que.append(item)
    result.append(que.popleft())
    
print(*result)
