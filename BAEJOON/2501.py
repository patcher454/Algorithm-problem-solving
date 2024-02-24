def find(N, K):
    for i in range(1, N + 1):
        if N % i == 0:
            K -= 1
            if K == 0:
                print(i)
                return
    print(0)


N, K = map(int, input().split())
find(N, K)
