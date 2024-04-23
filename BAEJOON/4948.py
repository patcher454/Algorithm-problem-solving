from sys import stdin

arr = [1 for i in range(123456 * 2 + 1)]
arr[0] = 0
arr[1] = 0


while True:
    n = int(stdin.readline()) * 2
    if(n != 0):
        i = 2 
        while i*i < n:
            if arr[i] == 1:
                j = i * 2
                while j<=n: 
                    arr[j] = 0;
                    j+=i
            i += 1
        print(sum(arr[n//2 + 1: n + 1]))
        continue
    break
    