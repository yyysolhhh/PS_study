n = int(input())
ans = 0
for _ in range(n):
    d = int(input())
    ans += 1 if d % 2 == 1 else 0
print(ans)