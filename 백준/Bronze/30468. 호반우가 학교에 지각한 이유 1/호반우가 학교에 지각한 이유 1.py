STR, DEX, INT, LUK, N = map(int, input().split())
stat = STR + DEX + INT + LUK
ans = 0
while stat // 4 < N:
    stat += 1
    ans += 1
print(ans)