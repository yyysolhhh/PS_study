money = (500, 100, 50, 10, 5, 1)
n = int(input())
change = 1000 - n
ans = 0
i = 0
while change:
    ans += change // money[i]
    change = change % money[i]
    i += 1
print(ans)