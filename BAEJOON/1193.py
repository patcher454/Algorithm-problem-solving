import math

num = int(input())
level = math.floor((-1.000001 + math.sqrt(1 + 8 * num)) / 2) + 1
levelMaxNum = int((level ** 2 + level) / 2)
dist = levelMaxNum - num

if level % 2 == 0:
    print(level - dist, "/", dist + 1 , sep = '')
else:
    print(dist + 1, "/", level - dist, sep = '')
