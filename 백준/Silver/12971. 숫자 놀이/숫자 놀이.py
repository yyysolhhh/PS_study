P1, P2, P3, X1, X2, X3 = map(int, input().split())
ans = -1
for N in range(P1 * P2 * P3):
    if N % P1 == X1 and N % P2 == X2 and N % P3 == X3:
        ans = N
        break
print(ans)