from sys import stdin

nums = [] 

n = int(stdin.readline())
for i in range(n):
    input = int(stdin.readline())
    
    if input == 0:
        del nums[len(nums) - 1]
        continue
    
    nums.append(input)
    
print(sum(nums))
