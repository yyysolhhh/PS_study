a, b, c, d, e = (int(input()) for _ in range(5))
ans = 0
if a < 0:
  ans += -a * c + d
  a = 0
ans += (b - a) * e
print(ans)