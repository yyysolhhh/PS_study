import sys
input = sys.stdin.readline
N, K, L = map(int, input().split())
ans = 0
member = []
for _ in range(N):
    x1, x2, x3 = map(int, input().split())
    if x1 >= L and x2 >= L and x3 >= L and x1 + x2 + x3 >= K:
        member.append(f"{x1} {x2} {x3}")
        ans += 1
print(ans)
print(*member)