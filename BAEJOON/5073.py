def test(sides):
    if sides[2] < sides[1] + sides[0]:
        sides = set(sides)
        if len(sides) == 1:
            print("Equilateral")
            return
        if len(sides) == 2:
            print("Isosceles")
            return
        print("Scalene")
        return
    print("Invalid")
   
while True:
    sides = list(map(int,input().split()))
    sides.sort()
   
    if(0 in sides):
        break
   
    test(sides)
