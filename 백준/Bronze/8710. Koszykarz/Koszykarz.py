k, w, m = map(int, input().split())
add = w - k
ans = add // m + (add % m > 0)
print(ans)