N = int(input())
diff = N // 2
left, right = diff, diff * 2
ans = []
for i in range(diff):
    ans.append(left)
    ans.append(right)
    left -= 1
    right -= 1
if N & 1:
    ans.append(N)
print(*ans)