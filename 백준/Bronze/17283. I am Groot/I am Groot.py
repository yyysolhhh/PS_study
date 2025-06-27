L = int(input())
R = int(input())
ans, i = 0, 1
while L > 5:
    L = int(L * R * 0.01)
    if L <= 5:
        break
    ans += L * 2 ** i
    i += 1
print(ans)