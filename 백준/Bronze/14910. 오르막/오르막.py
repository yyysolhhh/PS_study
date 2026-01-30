N = list(map(int, input().split()))
ans = "Good"
for i in range(len(N) - 1):
    if N[i] > N[i + 1]:
        ans = "Bad"
        break
print(ans)