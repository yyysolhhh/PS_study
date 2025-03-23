import sys
input = sys.stdin.readline

def binary_search(N, L, W, H):
    left, right = 0, min(L, W, H)
    for _ in range(100):
        mid = (left + right) / 2
        num = (L // mid) * (W // mid) * (H // mid)
        if num >= N:
            left = mid
        else:
            right = mid
    return left

N, L, W, H = map(int, input().split())
ans = binary_search(N, L, W, H)
print(f"{ans:.10f}")