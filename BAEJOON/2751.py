from sys import stdin
print(*sorted([int(stdin.readline()) for i in range(int(stdin.readline()))]), sep="\n")
