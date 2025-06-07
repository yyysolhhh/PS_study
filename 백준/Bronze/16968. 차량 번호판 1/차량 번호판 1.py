form = input()
num = {"d": 10, "c": 26}
ans = num[form[0]]
for i in range(1, len(form)):
    if form[i] == form[i - 1]:
        ans *= num[form[i]] - 1
    else:
        ans *= num[form[i]]
print(ans)