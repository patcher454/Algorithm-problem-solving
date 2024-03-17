def test():
    n = int(input())
    min = 100000000
    for i in range(n, 0, -1):
        if n == i + (sum(list(map(int,list(str(i)))))):
            if min > i:
                min = i
    if min != 100000000:
        return min
    return 0
    
print(test())
