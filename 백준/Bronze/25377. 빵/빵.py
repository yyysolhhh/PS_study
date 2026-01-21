from sys import stdin
n = int(stdin.readline().strip())
result = 1001
for i in range(n):
    a, b = map(int, stdin.readline().split())
    if b>=a:
        if b<result:
            result = b
if result == 1001:
    print(-1)
else:
    print(result)