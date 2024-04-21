from sys import stdin

def gcd(a,b):
    while b != 0:
        n = a % b
        a = b
        b = n

    return a

disArr = []

n = int(stdin.readline())
old = int(stdin.readline())
gcdValue = 0
for i in range(n - 1):
    new = int(stdin.readline())
    dis = new - old
    disArr.append(dis)
    if gcdValue == 0:
        gcdValue = dis
    gcdValue = gcd(gcdValue,dis)
    old = new

        
count = 0
for i in disArr:
    count += i / gcdValue - 1
print(int(count))
