visiting = list(map(int, input().split()))
home = list(map(int, input().split()))
score = [6, 3, 2, 1, 2]
v_score = sum(i * j for i, j in zip(visiting, score))
h_score = sum(i * j for i, j in zip(home, score))
print(v_score, h_score)