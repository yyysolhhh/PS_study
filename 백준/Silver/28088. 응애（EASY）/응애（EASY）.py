import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
eung = [0 for _ in range(N)]
for _ in range(M):
    first = int(input())
    eung[first] = 1
for _ in range(K):
    nxt = [0 for _ in range(N)]
    for i in range(N):
        if eung[i] == 1:
            nxt[(i + 1 + N) % N] ^= 1
            nxt[(i - 1 + N) % N] ^= 1
    eung = nxt
print(sum(eung))
