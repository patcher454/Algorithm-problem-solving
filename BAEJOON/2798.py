def test():
    n = int(input().split()[1])
    card_list = list(map(int, input().split()))

    selected_list = []

    min_dist = 10000000000 
    for i in card_list:
        for j in card_list:
            if j == i:
                continue
            for k in card_list:
                if k == i or k == j:
                    continue
                dist = n - (i + j + k)
                if dist >= 0 and dist < min_dist:
                    min_dist = dist
                    selected_list.clear()
                    selected_list.append(i)
                    selected_list.append(j)
                    selected_list.append(k)
                if dist == 0:
                    return sum(selected_list)
    return sum(selected_list)
    
print(test())