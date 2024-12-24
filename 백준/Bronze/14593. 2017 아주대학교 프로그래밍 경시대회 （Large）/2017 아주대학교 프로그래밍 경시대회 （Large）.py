N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]
sorted_score = sorted(score, key=lambda x:(-x[0], x[1], x[2]))
print(score.index(sorted_score[0])+1)