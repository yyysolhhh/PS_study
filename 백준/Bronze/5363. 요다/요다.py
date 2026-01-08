import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    sen = list(input().split())
    ans = sen[2:] + sen[:2]
    print(*ans)