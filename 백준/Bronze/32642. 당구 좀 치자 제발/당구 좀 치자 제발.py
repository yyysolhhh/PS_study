N = int(input())
weather = list(map(int, input().split()))
ans, anger = 0, 0
for i in weather:
    if i == 1:
        anger += 1
    else:
        anger -= 1
    ans += anger
print(ans)