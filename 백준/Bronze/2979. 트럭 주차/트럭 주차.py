A, B, C = map(int, input().split())
park = [0 for _ in range(100)]
fee = dict(zip((0, 1, 2, 3), (0, A, B, C)))
for _ in range(3):
    arri, leav = map(int, input().split())
    for i in range(arri, leav):
        park[i] += 1
ans = 0
for i in park:
    ans += fee[i] * i
print(ans)