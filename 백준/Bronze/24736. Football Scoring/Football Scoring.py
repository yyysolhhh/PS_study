visiting = list(map(int, input().split()))
home = list(map(int, input().split()))
v_score = 6 * visiting[0] + 3 * visiting[1] + 2 * visiting[2] + 1 * visiting[3] + 2 * visiting[4]
h_score = 6 * home[0] + 3 * home[1] + 2 * home[2] + 1 * home[3] + 2 * home[4]
print(v_score, h_score)