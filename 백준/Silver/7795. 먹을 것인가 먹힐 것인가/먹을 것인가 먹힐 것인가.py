import sys
input = sys.stdin.readline

def binarysearch(n):
    start, end = 0, len(B) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if B[mid] < n:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    ans = 0
    for i in A:
        ans += binarysearch(i) + 1
    print(ans)