N = int(input())
ans = 0
for num in range(1, N + 1):
    total = sum(int(i) for i in str(num))
    if total == 0:
        continue
    ans += (num % total == 0)
print(ans)