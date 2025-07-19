N = int(input())
A = list(map(int, input().split()))
ans = 0
cnt = [0 for _ in range(1001)]
for i in A:
    cnt[i] += 1
for i in cnt:
    ans += min(i, 2)
print(ans)