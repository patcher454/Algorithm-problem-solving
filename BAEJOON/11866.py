n, k = map(int, input().split())

list = list(range(1, n+1))
result = []
count = 1
selectedIndex = 0
while n != len(result):
    if count == k:
        result.append(list[selectedIndex])
        del list[selectedIndex]
        count = 1
        if len(list) <= selectedIndex:
            selectedIndex = 0
        continue
    
    count += 1
    
    if len(list) <= selectedIndex + 1:
        selectedIndex = 0
        continue
    
    selectedIndex += 1
    
print("<",end="")
print(*result, end=">",sep=", ")
