T = int(input())
for _ in range(T):
    N = int(input())
    mul = str(N ** 2)
    l = len(str(N))
    if mul[-l:] == str(N):
        print("YES")
    else:
        print("NO")