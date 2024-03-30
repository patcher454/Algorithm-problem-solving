from sys import stdin
nums = list(stdin.readline())
nums.remove('\n')
print(*sorted([int(i) for i in nums], reverse=True), sep="")