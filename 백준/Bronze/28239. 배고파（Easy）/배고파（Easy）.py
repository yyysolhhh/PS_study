import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m = int(input())
    for x in range(70):
        for y in range(x, 70):
            if 2 ** x + 2 ** y == m:
                print(x, y)