def getResult(list, item):
    if len(list) == 2:
        if list[0] == item:
            return list[1]
        return list[0]
    return item


xList = []
yList = []
for x in range(2):
    x, y = map(int, input().split())
    if x not in xList:
        xList.append(x)
    if y not in yList:
        yList.append(y)

x, y = map(int, input().split())
print(getResult(xList, x), getResult(yList, y))
