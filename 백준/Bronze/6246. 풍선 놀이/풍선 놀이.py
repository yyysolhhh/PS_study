N, Q = map(int, input().split())
slot = [0] + [1 for _ in range(1, N + 1)]
for _ in range(Q):
    L, I = map(int, input().split())
    for i in range(L, N + 1, I):
        slot[i] = 0
print(sum(slot))