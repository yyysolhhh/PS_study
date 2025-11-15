import sys
input = sys.stdin.readline
mul = [1 for _ in range(10)]
for i in range(1, 10):
    mul[i] = i * mul[i - 1]
while True:
    n = input().strip()
    if n == "0":
        break
    ans = 0
    for i, j in enumerate(n[::-1]):
        ans += int(j) * mul[int(i + 1)]
    print(ans)