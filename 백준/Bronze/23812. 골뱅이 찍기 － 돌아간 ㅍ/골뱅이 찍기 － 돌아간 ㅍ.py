N = int(input())
l1 = "@" * N + " " * N * 3 + "@" * N + "\n"
l2 = "@" * N * 5 + "\n"
print((l1 * N + l2 * N) * 2 + l1 * N)