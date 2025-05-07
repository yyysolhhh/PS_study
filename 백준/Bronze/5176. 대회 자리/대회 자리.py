K = int(input())
for _ in range(K):
    P, M = map(int, input().split())
    seats = [0 for _ in range(M + 1)]
    ans = 0
    for _ in range(P):
        a = int(input())
        if seats[a]:
            ans += 1
        seats[a] = 1
    print(ans)