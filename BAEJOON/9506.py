divisor = []
while True:
    divisor.clear()
    N = int(input())
    if N != -1:
        for i in range(1, int(N / 2) + 1):
            if N % i == 0:
                divisor.append(i)
        if sum(divisor) == N:
            print(N, "=", " + ".join(map(str, divisor)))
        else:
            print(N, "is NOT perfect.")
        continue
    break
