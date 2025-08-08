N = int(input())
seq = [int(input()) for _ in range(N)]
cha = 1
for i in range(1, N - 1):
    cha *= seq[i] - seq[i - 1] == seq[i + 1] - seq[i]
print(2 * seq[-1] - seq[-2] if cha else int(seq[-1] ** 2 / seq[-2]))