import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().strip() for _ in range(k)]
    ans = ""
    for i in range(k - 1):
        for j in range(i + 1, k):
            c1 = words[i] + words[j]
            c2 = words[j] + words[i]
            if c1 == "".join(reversed(c1)):
                ans = c1
            elif c2 == "".join(reversed(c2)):
                ans = c2
        if ans:
            break
    if ans:
        print(ans)
    else:
        print(0)