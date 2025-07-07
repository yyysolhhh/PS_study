N = input()
ans, cnt = 0, 0
for i in range(len(N) - 1):
    if N[i:i + 2] == "((":
        cnt += 1
    if N[i:i + 2] == "))":
        ans += cnt
print(ans)