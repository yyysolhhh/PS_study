k = input()
korea = "KOREA"
ans = 0
idx = 0
for i in k:
    if i == korea[idx]:
        ans += 1
        idx += 1
    if idx > 4:
        idx = 0
print(ans)