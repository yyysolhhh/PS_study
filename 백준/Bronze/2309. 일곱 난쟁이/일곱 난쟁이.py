tall = list(int(input()) for _ in range(9))
tall.sort()
sum_of_tall = sum(tall)
for i in range(9):
    for j in range(i+1, 9):
        if sum_of_tall - (tall[i] + tall[j]) == 100:
            if i == j:
                continue
            rmv1 = tall[i]
            rmv2 = tall[j]
            break
tall.remove(rmv1)
tall.remove(rmv2)
for i in tall:
    print(i)
