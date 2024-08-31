import sys, operator
input = sys.stdin.readline
yd = input()
N = int(input())
team = dict()
for _ in range(N):
    name = input()
    l = yd.count("L") + name.count("L")
    o = yd.count("O") + name.count("O")
    v = yd.count("V") + name.count("V")
    e = yd.count("E") + name.count("E")
    team[name] = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100
print(sorted(team.items(), key=lambda x: (-x[1], x[0]))[0][0])