num, baseString = input().split()

base = int(baseString)
result = 0

asc = 0  
dec = 0
for i in range(len(num)):
    asc = ord(num[i])
    
    if (48 <= asc <= 57):
        dec = int(num[i])
    else:
        dec = asc - 55
    
    result += dec * (base ** (len(num) - (i + 1)))
    
print(result)
