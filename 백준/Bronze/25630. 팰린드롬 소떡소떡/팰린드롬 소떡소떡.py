N = int(input())
st = input()
ans = 0
for i in range(N // 2):
    if st[i] != st[-i - 1]:
        ans += 1
print(ans)