def binary_search(start, end):
    for _ in range(100):
        mid = (start + end) / 2
        cnt = (L // mid) * (W // mid) * (H // mid)
        if cnt < N:
            end = mid
        else:
            start = mid
    return float(mid)


N, L, W, H = map(int, input().split())
start, end = 0, min(L, W, H)
print(binary_search(start, end))
