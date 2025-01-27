def solve(n):
    if int(n ** 0.5) ** 2 == n:
        return 1
    return 0

N = int(input())
X = list(map(int, input().split()))
ans = map(solve, X)
print(*ans)