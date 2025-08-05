import string
mo = "AEIOU"
N, M = map(int, input().split())
S = input()
ans = True
name = ""
i = N - 1
while S[i] in mo:
    if i < 0:
        ans = False
        break
    i -= 1
name = S[i]
i -= 1
while S[i] != "A":
    if i < 0:
        ans = False
        break
    i -= 1
name = S[i] + name
i -= 1
while S[i] != "A":
    if i < 0:
        ans = False
        break
    i -= 1
if i < M - 4:
    ans = False
else:
    print(i, S[i], S[i - M])
    name = S[i - M + 3:i + 1] + name
print(f"YES\n{name}" if ans else "NO")