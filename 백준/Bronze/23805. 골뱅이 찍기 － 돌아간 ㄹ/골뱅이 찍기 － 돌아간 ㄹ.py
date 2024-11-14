N = int(input())
ans = ['' for _ in range(N * 5)]
for i in range(N * 5):
    if i < N:
        ans[i] = "@" * N * 3 + " " * N + "@" * N
    elif N <= i < N * 4:
        ans[i] = ("@" * N + " " * N) * 2 + "@" * N
    else:
        ans[i] = "@" * N + " " * N + "@" * N * 3
print("\n".join(ans))