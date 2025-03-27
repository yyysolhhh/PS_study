a, b, n, w = map(int, input().split())
def solve():
    sheep = -1
    for i in range(1, n):
        if i * a + (n - i) * b == w:
            if sheep == -1:
                sheep = i
            else:
                return -1
    return sheep
ans = solve()
if ans == -1:
    print(ans)
else:
    print(ans, n - ans)