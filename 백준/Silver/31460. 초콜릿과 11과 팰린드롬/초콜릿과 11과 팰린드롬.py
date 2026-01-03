T = int(input())
for _ in range(T):
    N = int(input())
    if N > 1:
        ans = "1" + "2" * (N - 2) + "1"
    else:
        ans = "0"
    print(ans)