now = input()
N = int(input())
ans = 0
for _ in range(N):
    ans += now <= input()
print(ans)