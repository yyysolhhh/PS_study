n = int(input())
m = int(input())
a = list(map(int, input().split()))
ans = [0 for _ in range(n)]
for i in range(m):
    b = list(map(int, input().split()))
    for j, b in enumerate(b):
        if b == a[i]:
            ans[j] += 1
        else:
            ans[a[i] - 1] += 1
for i in ans:
    print(i)