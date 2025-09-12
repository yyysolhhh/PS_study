N = int(input())
S = input()
ans = 0
for i in range(N):
    if S[i] == "A":
        n, l = 0, 1
        for j in range(i + 1, N):
            if S[j] == "A":
                break
            if S[j] == "N":
                n += 1
            l += 1
        else:
            continue
        if l >= 2 and n == 1:
            ans += 1
print(ans)