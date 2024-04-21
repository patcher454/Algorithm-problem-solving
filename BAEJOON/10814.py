from sys import stdin

dict = {}

for i in range(int(stdin.readline())):
    age, name = map(str,stdin.readline().replace("\n", "").split())
    age = int(age)
    if age not in dict:
        dict[age] = []
    dict[age].append(name)

for age in sorted(dict):
    for name in dict[age]:
        print(age, name)