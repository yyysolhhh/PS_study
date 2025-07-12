import sys

N = int(sys.stdin.readline())

score_list = sorted([float(sys.stdin.readline()) for _ in range(N)])

for i in range(7):
    print(f'{score_list[i]:.3f}')