plates = input()
ans = 10
for i, j in zip(plates, plates[1:]):
    if i == j:
        ans += 5
    else:
        ans += 10
print(ans)