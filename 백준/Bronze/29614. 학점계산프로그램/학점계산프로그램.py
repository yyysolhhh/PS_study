S = input()
grades = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
ans = 0
cnt = 0
for i in range(len(S)):
    if S[i] == "+":
        continue
    grade = 0
    if i + 1 < len(S) and S[i + 1] == "+":
        grade += 0.5
    grade += grades[S[i]]
    ans += grade
    cnt += 1
ans /= cnt
print(round(ans, 5))