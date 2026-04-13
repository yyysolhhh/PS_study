K = int(input())
mag = input()
ans = 0
for i in range(1, K):
    if mag[i] != mag[i - 1]:
        r, l = 1, 1
        j = i
        while j < K - 1 and mag[j] == mag[j + 1]:
            r += 1
            j += 1
        j = i - 1
        while j > 0 and mag[j] == mag[j - 1]:
            l += 1
            j -= 1
        ans = max(ans, min(r, l))
ans *= 2
print(ans)
