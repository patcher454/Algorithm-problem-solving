items = [int(input())]
for i in range(4):
    n = int(input())
    for j in range(len(items)):
        if n < items[j]:
            items.insert(j, n)
            break
    if i + 1 == len(items):
        items.append(n)

print(sum(items) // 5)
print(items[2])
