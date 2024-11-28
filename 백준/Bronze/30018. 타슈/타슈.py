N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i, j in zip(a, b):
    if i < j:
        ans += j - i
print(ans)