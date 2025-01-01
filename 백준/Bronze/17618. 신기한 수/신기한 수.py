N = int(input())
ans = 0
for num in range(1, N + 1):
    total = 0
    for i in str(num):
        total += int(i)
    if total == 0:
        continue
    ans += (num % total == 0)
print(ans)