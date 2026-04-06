N = int(input())
poke = dict()
ans = 0
for _ in range(N):
    P = input()
    K, M = map(int, input().split())
    poke[P] = 0
    while M >= K:
        ans += 1
        poke[P] += 1
        M -= K - 2
print(ans)
print(sorted(poke.items(), key=lambda x: -x[1])[0][0])
