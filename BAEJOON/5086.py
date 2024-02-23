def test(A,B):
    if A < B:
        if B % A == 0:
            print("factor")
            return
    else:
        if A % B == 0:
            print("multiple")
            return
    print("neither")
​

while(True):
    A, B = map(int, input().split())
    if(A == 0):
        break
    test(A, B)
