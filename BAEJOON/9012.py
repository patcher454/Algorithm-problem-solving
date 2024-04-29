from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    st = []
    line = stdin.readline()
    for i in line:
        if "(" == i:
            st.append(i)
            continue
        
        if ")" == i:
            if len(st) > 0:
                del st[len(st) - 1]
                continue
            st.append(" ")
            break
        
    if len(st) != 0:
        print("NO")
        continue
    print("YES")
    