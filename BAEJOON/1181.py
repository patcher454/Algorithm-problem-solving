from sys import stdin

dict = {}

for i in range(int(stdin.readline())):
    word = stdin.readline().replace("\n", "")
    if len(word) not in dict:
        dict[len(word)] = []
    if word in dict[len(word)]:
        continue
    dict[len(word)].append(word)

for len in sorted(dict):
    for word in sorted(dict[len]):
        print(word)