def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
r = list(map(int, input().split()))
for i in r[1:]:
    g = gcd(r[0], i)
    print(f"{r[0] // g}/{i // g}")