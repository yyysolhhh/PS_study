N = int(input())
for _ in range(N):
    M = int(input())
    mission = []
    for _ in range(M):
        K, D, A = map(int, input().split())
        mission.append((K, D, A))
    k, d, a = map(int, input().split())
    ans = 0
    for x, y, z in mission:
        temp = x * k - y * d + z * a
        if temp > 0:
            ans += temp
    print(ans)