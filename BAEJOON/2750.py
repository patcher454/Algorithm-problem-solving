n = int(input())
items = []
sot = []
for i in range(n):
    items.append(int(input()))
    
count = len(items)
for i in range(count):
    item = min(items)
    sot.append(item)
    items.remove(item)
    

for i in sot: 
    print(i) 
