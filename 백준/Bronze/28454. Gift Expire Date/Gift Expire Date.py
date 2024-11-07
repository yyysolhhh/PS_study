now = list(map(int, input().split('-')))
N = int(input())
ans = 0
for _ in range(N):
    exp = list(map(int, input().split('-')))
    if now[0] < exp[0]:
        ans += 1
    elif now[0] == exp[0]:
        if now[1] < exp[1]:
            ans += 1
        elif now[1] == exp[1]:
            if now[2] <= exp[2]:
                ans += 1
print(ans)