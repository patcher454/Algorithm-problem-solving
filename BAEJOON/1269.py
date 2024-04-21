from sys import stdin
stdin.readline()

A = set(stdin.readline().split())
B = set(stdin.readline().split())
print(len(A-B) + len(B-A))