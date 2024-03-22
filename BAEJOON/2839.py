n = int(input())
n5 = n // 5 + 1
min = 5000

for i in range(n5):
    count = i
    tmp = n - (i * 5)
    if tmp < 0:
        continue
    count += tmp // 3
    if tmp % 3 != 0:
        continue
    if min > count:
        min = count
        
if min == 5000 or min == 0:
    print(-1)
else:
    print(min)
