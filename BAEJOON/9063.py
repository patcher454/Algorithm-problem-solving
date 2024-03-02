N = int(input())

minX, maxX = 10000, -10000
minY, maxY = 10000, -10000
for i in range(N):
    x, y = map(int, input().split())
    if minX > x:
        minX = x
        
    if minY > y:
        minY = y
    
    if maxX < x:
        maxX = x

    if maxY < y:
        maxY = y
        

print((maxX - minX) * (maxY - minY))        
