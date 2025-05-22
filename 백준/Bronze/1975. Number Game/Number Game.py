import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    for i in range(2, N + 1):
        x = N
        while x:
            if x % i == 0:
                ans += 1
                x //= i
            else:
                break
    print(ans)