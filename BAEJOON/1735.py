from sys import stdin

def gcd(a,b):
    while b != 0:
        n = a % b
        a = b
        b = n
        
    return a

a1, b1 = map(int, stdin.readline().split())
a2, b2 = map(int, stdin.readline().split())

a, b = a1 * b2 + a2 * b1, b1 * b2

g = gcd(a, b)
print(a // g, b // g)
