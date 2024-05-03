from collections import deque

n = int(input())

q = deque(list(range(1, n + 1)))
while len(q) != 1:
    q.popleft()
    num = q.popleft()
    q.append(num)
    
print(q[0])
