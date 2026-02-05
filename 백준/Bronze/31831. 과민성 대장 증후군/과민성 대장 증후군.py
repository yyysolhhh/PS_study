N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt, total = 0, 0
for i in A:
    if total >= 0:
        if total + i < 0:
            total = 0
        else:
            total += i
    else:
        if total - i < 0:
            total = 0
        else:
            total -= i
    if total >= M:
        cnt += 1
print(cnt)