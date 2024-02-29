import math

N = int(input())
d = 2

MaxDiv = math.sqrt(N)
while d <= MaxDiv:
    if N % d != 0:
        d += 1
        continue

    print(d)
    N //= d

if N > 1:
    print(N)
