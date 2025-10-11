n, m = map(int, input().split())
baguni = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    baguni = baguni[:i] + list(reversed(baguni[i:j + 1])) + baguni[j + 1:]
print(*baguni[1:])