a, b = map(int, input().split())
ans = 1
for i in range(a, b + 1):
    ans *= (1 + i) * i // 2
print(ans % 14579)
