T = int(input())
for _ in range(T):
    S = set(input())
    ans = sum(i for i in range(65, 91))
    for i in S:
        ans -= ord(i)
    print(ans)
