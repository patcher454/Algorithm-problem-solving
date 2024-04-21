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

n, n1 = map(int, stdin.readline().split())
lastPrime = findPrimeNum(n)
while n1 >= lastPrime:
    print(lastPrime)
    lastPrime = findPrimeNum(lastPrime + 1)

