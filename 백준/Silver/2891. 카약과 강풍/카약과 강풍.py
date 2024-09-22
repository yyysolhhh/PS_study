import sys
input = sys.stdin.readline
N, S, R = map(int, input().split())
t_broken = set(map(int, input().split()))
t_more = set(map(int, input().split()))
intersection = t_broken & t_more
t_broken -= intersection
t_more -= intersection
ans = 0
for i in t_broken:
    if i - 1 in t_more:
        t_more.remove(i - 1)
    elif i + 1 in t_more:
        t_more.remove(i + 1)
    else:
        ans += 1
print(ans)