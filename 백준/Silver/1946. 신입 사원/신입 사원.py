import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    appl = [list(map(int, input().split())) for _ in range(N)]
    appl.sort()
    cnt = 1
    rank = appl[0][1]
    for i in range(1, N):
        if rank > appl[i][1]:
            cnt += 1
            rank = appl[i][1]
    print(cnt)