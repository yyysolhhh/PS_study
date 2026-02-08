k = int(input())
ans = 25 + k * 0.01
if ans < 100:
    ans = 100
if ans > 2000:
    ans = 2000
print(f"{ans:.2f}")