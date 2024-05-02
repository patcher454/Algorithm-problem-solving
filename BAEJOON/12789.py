from sys import stdin

def test():
    n = int(stdin.readline())
    list = map(int, stdin.readline().split())

    lookingFor = 1
    st = []
    for i in list:
        if lookingFor == i:
            lookingFor += 1 
            continue
    
        while len(st) > 0 and st[0] == lookingFor:
            lookingFor += 1
            del st[0]
        
        st.insert(0, i)
    
    for i in st:
        if lookingFor == i:
            lookingFor += 1
            continue
    
        print("Sad")
        return
    print("Nice")

    

test()