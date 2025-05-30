T = int(input())
for _ in range(T):
    ans = "NOT CHEATER"
    n = int(input())
    cards = sorted(input().split())
    after = sorted(input().split())
    for i, j in zip(cards, after):
        if i != j:
            ans = "CHEATER"
    print(ans)