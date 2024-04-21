from sys import stdin

input = stdin.readline().strip()
resultSet = set()

for i in range(len(input)):
    for j in range(i, len(input)):
        resultSet.add(input[i:j+1])
        
print(len(resultSet))