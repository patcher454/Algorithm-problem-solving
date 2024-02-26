import math

N = int(input())
num = list(map(int, input().split())) 
cnt = 0

for i in range(N):
    if num[i] == 1:
        continue
    
    j = 0
    for j in range(1, int(math.sqrt(num[i]))+1):
        if ((num[i] % j == 0) and (j != 1)): 
            j -= 1
            break

    if ( (j == int(math.sqrt(num[i]))) and (num[i] != (j*j))):
        cnt += 1

print(cnt)
