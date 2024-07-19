import sys
from itertools import combinations
input = sys.stdin.readline
while True:
    case = list(map(int, input().split()))
    if case == [0]:
        break
    lotto = list(combinations(case[1:], 6))
    for i in lotto:
        print(*i)
    print()