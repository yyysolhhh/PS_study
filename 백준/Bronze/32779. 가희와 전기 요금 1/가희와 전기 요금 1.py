Q = int(input())
for _ in range(Q):
    a, m = map(int, input().split())
    print(1056 * a * m // (10000 * 60))