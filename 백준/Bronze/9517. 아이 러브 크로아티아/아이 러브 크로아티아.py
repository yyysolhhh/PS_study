K = int(input())
N = int(input())
ans = K
time = 0
q = [input().split() for _ in range(N)]
for T, Z in q:
    time += int(T)
    if time >= 210:
        break
    if Z == "T":
        ans = (ans + 1) % 9
        if ans == 0:
            ans = 1
print(ans)