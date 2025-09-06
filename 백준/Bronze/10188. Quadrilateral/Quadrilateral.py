import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    w, l = map(int, input().split())
    for _ in range(l):
        print("X" * w)
    print()