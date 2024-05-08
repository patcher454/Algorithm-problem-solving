n = int(input())
b = list(range(1, n + 1))
seq = list(map(int, input().split()))
result = []

count = 0
selectedIndex = 0

def updateCount():
    global count
    if count < 0:
        count += 1
        return
    
    if count > 0:
        count -= 1 
        return
    
def updateIndex():
    global count
    global selectedIndex
    global b
    
    if count < 0:
        if selectedIndex - 1 < 0:
            selectedIndex = len(b) - 1
            return
        selectedIndex -= 1 
        return
    
    if count > 0:
        if selectedIndex + 1 >= len(b):
            selectedIndex = 0
            return
        selectedIndex += 1
        return
    
while len(b) != 1:
    if count == 0:
        result.append(b[selectedIndex])
        del b[selectedIndex]
        count = seq[result[-1] - 1]
        if count < 0 or len(b) <= selectedIndex:
            updateIndex()
        updateCount()

        
    if(count != 0):
        updateIndex()
        updateCount()
    
result.append(b[0])
print(*result)
