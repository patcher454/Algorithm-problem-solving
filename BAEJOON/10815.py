from sys import stdin
stdin.readline()
nSet = set(stdin.readline().split())

stdin.readline()
result = []
for item in stdin.readline().split():
    result.append(1 if item in nSet else 0)

print(*result)