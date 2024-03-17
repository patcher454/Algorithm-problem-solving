def test():
    a, b, c, d, e, f = map(int, input().split())
    for x in range(-999, 1000, 1):
        for y in range(-999, 1000, 1):
            if a * x + b * y - c == 0 and d * x + e * y - f == 0:
                print(x, y)
                return
test()