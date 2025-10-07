import sys
input = sys.stdin.readline
N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
def binary(i, A, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if i == A[mid]:
        return 1
    elif i < A[mid]:
        return binary(i, A, start, mid-1)
    else:
        return binary(i, A, mid+1, end)
for i in nums:
    start = 0
    end = len(A) - 1
    print(binary(i, A, start, end))
