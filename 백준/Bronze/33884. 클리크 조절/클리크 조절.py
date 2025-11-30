import sys
input = sys.stdin.readline
N = int(input())
first = sorted(tuple(map(int, input().split())) for _ in range(N))
second = sorted(tuple(map(int, input().split())) for _ in range(N))
print(second[0][0] - first[0][0], second[0][1] - first[0][1])