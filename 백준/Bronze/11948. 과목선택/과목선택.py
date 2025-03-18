ans = 0
temp = []
for _ in range(4):
    temp.append(int(input()))
temp.sort()
ans += sum(temp[1:])
temp = []
for _ in range(2):
    temp.append(int(input()))
ans += max(temp)
print(ans)