import sys
input = sys.stdin.readline

def solve(a, b):
    units = a % 10
    if units == 0:
        return 10
    elif units == 1 or units == 5 or units == 6:
        return units
    elif units == 4 or units == 9:
        if b % 2:
            return units
        else:
            return units * units % 10
    else:
        if not b % 4:
            return (units ** 4) % 10
        else:
            return units ** (b % 4) % 10

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(solve(a, b))