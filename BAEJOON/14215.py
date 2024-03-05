def sum_sides():
    sides = list(map(int, input().split()))
    max_side = max(sides)
    sides.remove(max_side)
    sum_sides = sum(sides)
    if max_side >= sum_sides:
        return sum_sides * 2 - 1
    return max_side + sum_sides
print(sum_sides())
