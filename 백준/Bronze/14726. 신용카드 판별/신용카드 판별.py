T = int(input())
for _ in range(T):
    card = list(map(int, input()))
    ans = 0
    for i in range(15, -1, -1):
        if i & 1 == 0:
            card[i] *= 2
        if card[i] >= 10:
            card[i] = card[i] // 10 + card[i] % 10
        ans += card[i]
    if ans % 10 == 0:
        print("T")
    else:
        print("F")