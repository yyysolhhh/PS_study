import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    sen = input().split()
    ans = sen[2:] + sen[:2]
    print(*ans)