import sys
lines = sys.stdin.readlines()
for line in lines:
    A, B, C = map(int, line.split())
    ans = max(C - B, B - A) - 1
    print(ans)