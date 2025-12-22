import sys
input = sys.stdin.readline
T = int(input())
period = 28
for _ in range(T):
    N = int(input())
    x = (N - 1) % period
    if x <= 14:
        value = x + 1
    else:
        value = period - x + 1
    binary = format(value, '04b')
    for i in binary:
        print("V" if i == '0' else "딸기", end="")
    print()