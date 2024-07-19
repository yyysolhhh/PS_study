import sys
def countNum(n, num):
    count = 0
    div = num
    while n >= div:
        count += n // div
        div *= num
    return count
n, m = map(int, sys.stdin.readline().split())
result = min(countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5),
             countNum(n, 2) - countNum(m, 2) - countNum(n-m, 2))
print(result)
