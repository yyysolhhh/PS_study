import sys
input = sys.stdin.readline
n = int(input())
students = []
for _ in range(n):
    line = input().strip().split()
    name = line[0]
    score, risk, cost = map(int, line[1:])
    sch = score ** 3 // (cost * (risk + 1))
    students.append((sch, cost, name))
students.sort(key=lambda x: (-x[0], x[1], x[2]))
print(students[1][2])