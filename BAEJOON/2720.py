lineCount = int(input())

result = []
currency = [25, 10, 5, 1]
for i in range(lineCount):
    result.append([0, 0, 0, 0])
    change = int(input())

    for cnt, val in enumerate(currency):
        result[i][cnt], change = divmod(change, currency[cnt])
        if change == 0:
            break

for i in range(lineCount):
    print(*result[i])
