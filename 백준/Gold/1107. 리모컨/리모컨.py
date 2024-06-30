N = int(input())
M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()
result = abs(N - 100)
for i in range(1000000):
    for j in str(i):
        if j in broken:
            break
    else:
        result = min(result, len(str(i)) + abs(N - i))
print(result)