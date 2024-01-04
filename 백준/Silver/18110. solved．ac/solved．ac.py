import sys
input = sys.stdin.readline

def real_round(num):
    if 0.5 <= num - int(num):
        return int(num) + 1
    else:
        return int(num)

def decide_degree(n, op):
    if n == 0:
        return 0
    else:
        op.sort()
        exclude = real_round(n * 0.15)
        degree = real_round(sum(op[exclude:n-exclude]) / (n - 2 * exclude))
        return degree

n = int(input())
op = []
for _ in range(n):
    op.append(int(input()))
print(decide_degree(n, op))