grades = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
extra = {"+": 0.3, "0": 0, "-": -0.3}
N = int(input())
ans = 0
total = 0
for _ in range(N):
    name, credit, grade = input().split()
    if grade == "F":
        total += float(credit)
        continue
    ans += float(credit) * (float(grades[grade[0]]) + float(extra[grade[1]]))
    total += float(credit)
ans = round(ans / total + 10 ** -10, 2)
print("%.2f" % (ans))