import sys
input = sys.stdin.readline
ans = 0
scores = [int(input()) for _ in range(10)]
for i in range(10):
    ans += scores[i]
    if ans >= 100:
        break
if ans - 100 > 100 - (ans - scores[i]):
    ans = ans - scores[i]
print(ans)