N, K = map(int, input().split())
seq = list(map(int, input().split(",")))
for _ in range(K):
    temp = []
    for i in range(len(seq) - 1):
        temp.append(seq[i + 1] - seq[i])
    seq = temp
print(*seq, sep=",")