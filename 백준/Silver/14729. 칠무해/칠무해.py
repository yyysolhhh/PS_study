import sys
input = sys.stdin.readline
N = int(input())
scores = [float(input()) for _ in range(N)]
for i in sorted(scores)[:7]:
    print(f"{i:.3f}")