import sys
input = sys.stdin.readline
four = {0: "N", 1: "E", 2: "S", 3: "W"}
d = 0
for _ in range(10):
    t = int(input())
    if t == 1:
        d += 1
    elif t == 2:
        d += 2
    elif t == 3:
        d -= 1
print(four[d % 4])
