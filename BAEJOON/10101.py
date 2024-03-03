def test():
    deg = []
    sum = 0
    eqCount = 0
    for i in range(3):
        x = int(input())
    
        sum += x
    
        if x in deg:
            eqCount += 1
            continue

        deg.append(x)

    if sum == 180:
        if eqCount == 1:
            return "Isosceles"
        if eqCount == 2:
            return "Equilateral"
        return "Scalene"
    return "Error" 

print(test())
