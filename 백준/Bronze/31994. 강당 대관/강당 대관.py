max_n = 0
for _ in range(7):
    name, num = input().split()
    if max_n < int(num):
        ans = name
        max_n = int(num)
print(ans)