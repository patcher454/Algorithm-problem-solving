from sys import stdin

people = set()
n = int(stdin.readline())
for i in range(n):
    name, state = stdin.readline().split()
    if state == "enter":
        people.add(name)
        continue
    
    people.remove(name)
    
print(*sorted(people, reverse=True), sep="\n")
    