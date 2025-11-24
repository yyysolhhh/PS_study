N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = []
for a, b in zip(A, B):
    if a == b:
        if res[-1] == 1:
            res.append(2)
        else:
            res.append(1)
    elif a - b == 1 or a - b == -2:
        res.append(1)
    else:
        res.append(2)
ans, tmp = 1, 1
for i in range(N - 1):
    if res[i] == res[i + 1]:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 1
ans = max(ans, tmp)
print(ans)