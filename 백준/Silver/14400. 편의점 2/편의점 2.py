n = int(input())
customers = [tuple(map(int, input().split())) for _ in range(n)]
customers.sort()
mid_x = customers[n // 2][0]
customers.sort(key=lambda x: x[1])
mid_y = customers[n // 2][1]
ans = 0
for i, j in customers:
    ans += abs(i - mid_x) + abs(j - mid_y)
print(ans)