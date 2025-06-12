S = input()
ans = 1
for i in range(1, len(S)):
    if ord(S[i - 1]) >= ord(S[i]):
        ans += 1
print(ans)