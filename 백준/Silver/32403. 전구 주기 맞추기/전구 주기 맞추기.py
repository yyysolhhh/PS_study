N, T = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in a:
    num = 0
    while True:
        if T % (i + num) == 0 or T % (i - num) == 0:
            break
        else:
            num += 1
    ans += num
print(ans)