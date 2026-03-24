import sys
input = sys.stdin.readline

def constellation(m, d):
    g1 = [1, 4]
    g2 = [2]
    g3 = [3, 5]
    g4 = [6, 12]
    if m in g1:
        if d < 20:
            m -= 1
            if m == 0:
                m = 12
    elif m in g2:
        if d < 19:
            m -= 1
    elif m in g3:
        if d < 21:
            m -= 1
    elif m in g4:
        if d < 22:
            m -= 1
    else:
        if d < 23:
            m -= 1
    return m

birth = [0 for _ in range(13)]
for _ in range(7):
    m, d = map(int, input().split())
    birth[constellation(m, d)] += 1
N = int(input())
ans = []
for _ in range(N):
    m, d = map(int, input().split())
    if birth[constellation(m, d)] > 0:
        continue
    ans.append((m, d))
if len(ans) == 0:
    print("ALL FAILED")
else:
    ans.sort()
    for m, d in ans:
        print(m, d)
