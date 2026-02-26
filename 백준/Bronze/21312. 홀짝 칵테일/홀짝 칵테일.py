cocktails = list(map(int, input().split()))
odds = []
ans = 1
for i in cocktails:
    if i % 2 == 1:
        odds.append(i)
if len(odds) == 0:
    for i in cocktails:
        ans *= i
else:
    for i in odds:
        ans *= i
print(ans)