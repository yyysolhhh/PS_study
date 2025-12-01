T = int(input())
for _ in range(T):
    s, p = input().split()
    cnt = s.count(p)
    ans = cnt + len(s) - cnt * len(p)
    print(ans)