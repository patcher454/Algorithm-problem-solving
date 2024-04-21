from sys import stdin

def gcd(a,b):
    while b != 0:
        n = a % b
        a = b
        b = n
        
    return a
        


a, b = map(int, stdin.readline().split())
if a < b:
    tmp = a
    a = b
    b = tmp

print(int(a * b / gcd(a, b)))