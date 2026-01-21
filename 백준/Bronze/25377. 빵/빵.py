N = int(input())
time = 10000
ans = -1
for _ in range(N):
    A, B = map(int, input().split())
    if B - A >= 0 and time > B - A :
        ans = B
print(ans)