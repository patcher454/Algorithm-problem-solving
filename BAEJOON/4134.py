from sys import stdin
import math

def findPrimeNum(num):
    if num <= 2:
        return 2
    if num == 3:
        return 3
    
    while True:
        for i in range(2, int(math.sqrt(num)) + 3):
            if num % i == 0:
                isPrime = False
                num += 1
                break
            
            isPrime = True
            
        if isPrime:
            return num

n = int(stdin.readline())
for i in range(n):
    input = int(stdin.readline())
    print(findPrimeNum(input))
