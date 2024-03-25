n, cut = map(int, input().split())
points = list(map(int, input().split()))
cutPoint = 0
for i in range(cut):
    max = 0
    for point in points:
        if point > max:
            max = point
    points.remove(max)
    cutPoint = max

print(cutPoint)