from sys import stdin

stdin.readline()
nums = list(map(int, stdin.readline().split()))
keys = sorted(list(set(nums))) 

dict = {}
count = 0
for key in keys:
    dict[key] = count
    count += 1

result = []
for num in nums:
    result.append(dict[num])
    
print(*result)