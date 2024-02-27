import math

def test(M, N):
    min = 0
    sum = 0
    numList = list(range(M, N + 1))
    
    
    for num in numList:
        if num == 1:
            continue
        
        j = 0
        for j in range(1, int(math.sqrt(num))+1):
            if ((num % j == 0) and (j != 1)):
                j -= 1
                break
        
        if ( (j == int(math.sqrt(num))) and (num != (j*j))):
            if min == 0:
                min = num
            sum += num
    if(sum != 0):
        print(sum)
        print(min)
        return
    
    print(-1)


M = int(input())
N = int(input())
test(M,N)
