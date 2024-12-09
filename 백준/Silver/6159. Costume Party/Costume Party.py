N, S = map(int, input().split())
L = []
ans = 0
for _ in range(N):
    L.append(int(input()))
L.sort()
start = 0
end = N - 1
while start < end:
    if L[start] + L[end] > S:
        end -= 1
    else:
        ans += end - start
        start += 1
print(ans)