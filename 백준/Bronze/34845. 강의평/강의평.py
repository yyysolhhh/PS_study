N, X = map(int, input().split())
A = list(map(int, input().split()))
tot, cnt = sum(A), 0
avg = sum(A) / N
while avg < X:
    tot += 100
    cnt += 1
    avg = tot / (N + cnt)
print(cnt)