score = [6, 3, 2, 1, 2]
for _ in range(2):
    team = list(map(int, input().split()))
    print(sum(i * j for i, j in zip(team, score)), end=" ")