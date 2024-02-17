def toChar(num):
    if(num <= 9):
        return str(num)
    return chr(num + 55)


num, base = map(int, input().split())

if num != 0:
    result = ""
    while True:
        num, re = divmod(num, base)

        if(num < base):
            result += toChar(re)
            if num != 0:
                result += toChar(num)
            break

        result += toChar(re)

    print(result[::-1])
else:
    print("0")
