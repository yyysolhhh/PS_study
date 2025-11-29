import sys
input = sys.stdin.readline
N = int(input())
classroom = []
ans = 0
for _ in range(N + 1):
    classroom.append(input().strip().split())
classroom.sort(key=lambda x: (x[0], -ord(x[1][0])))
time = input().strip()
late, t = 0, 0
for i in range(N + 1):
    if classroom[i][0] < time:
        late = i
    if classroom[i][1] == "teacher":
        t = i
if late > t:
    print(N - late)
else:
    print(N - t)