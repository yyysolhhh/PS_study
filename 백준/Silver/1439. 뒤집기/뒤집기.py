s = input()
res = 1
for i, c in enumerate(s[1:]):
    if c != s[i]:
        res += 1
print(res // 2)