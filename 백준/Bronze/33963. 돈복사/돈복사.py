N = input()
d = len(N)
num = int(N)
ans = -1
while len(str(num)) <= d:
    num *= 2
    ans += 1
print(ans)