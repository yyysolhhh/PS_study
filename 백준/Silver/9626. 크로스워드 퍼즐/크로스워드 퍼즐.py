import sys
input = sys.stdin.readline
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
deco = "#." * 30
words = [input().strip() for _ in range(M)]
for i in range(U):
    print(deco[i % 2:L + R + N + i % 2])
for i in range(U, U + M):
    print(deco[i % 2:L + i % 2] + words[i - U] + deco[L + N + i % 2:L + N + R + i % 2])
for i in range(U + M, U + M + D):
    print(deco[i % 2:L + R + N + i % 2])