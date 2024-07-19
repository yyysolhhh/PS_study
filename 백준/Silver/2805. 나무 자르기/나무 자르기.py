import sys
input = sys.stdin.readline
N, M = map(int, input().split())
height = sorted(map(int, input().split()))
start = 0
end = height[-1]
while start <= end:
    mid = (start + end) // 2
    cut = 0
    cut = sum(i - mid for i in height if i - mid > 0)
    if cut < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)