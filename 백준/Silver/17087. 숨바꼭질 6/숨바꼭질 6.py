import sys
input = sys.stdin.readline
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
N, S = map(int, input().split())
A = list(map(int, input().split()))
D = list(set(abs(i-S) for i in A))
ans = D[0]
for i in range(1, len(D)):
    ans = gcd(ans, D[i])
print(ans)
