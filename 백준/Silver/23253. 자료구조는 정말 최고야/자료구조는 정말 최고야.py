import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = "Yes"
for _ in range(M):
    k = int(input())
    dummy = list(map(int, input().split()))
    for i in range(k - 1):
        if dummy[i + 1] - dummy[i] > 0:
            ans = "No"
            break
print(ans)