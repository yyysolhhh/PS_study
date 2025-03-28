N = int(input())
ans = 0
for A in range(2, N, 2):
    for B in range(1, N):
        for C in range(B + 2, N):
            if A + B + C != N:
                continue
            ans += 1
print(ans)