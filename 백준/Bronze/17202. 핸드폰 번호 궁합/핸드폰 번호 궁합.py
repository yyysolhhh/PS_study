A = input()
B = input()
ans = []
for i, j in zip(A, B):
    ans.append(int(i))
    ans.append(int(j))
while len(ans) > 2:
    tmp = []
    for i in range(len(ans) - 1):
        tmp.append((ans[i] + ans[i + 1]) % 10)
    ans = tmp
print("".join(map(str, ans)))
