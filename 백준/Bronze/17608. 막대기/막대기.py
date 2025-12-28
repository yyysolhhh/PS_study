import sys
input = sys.stdin.readline
N = int(input())
sticks = [int(input()) for _ in range(N)]
max_h = sticks[-1]
ans = 1
for i in sticks[-2::-1]:
    if i > max_h:
        ans += 1
        max_h = i
print(ans)