import sys
input = sys.stdin.readline
def convert(i):
    if 0 <= i < 510000:
        return 35
    elif i < 1020000:
        return 111
    elif i < 1530000:
        return 43
    elif i < 2040000:
        return 45
    else:
        return 46
N, M = map(int, input().split())
for _ in range(N):
    row = list(map(int, input().split()))
    for i in range(0, len(row), 3):
        intensity = 2126 * row[i] + 7152 * row[i + 1] + 722 * row[i + 2]
        print(chr(convert(intensity)), end="")
    print()