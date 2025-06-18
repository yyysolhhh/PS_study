while True:
    try:
        N, B, M = map(float, input().split())
        ans, money = 0, N
        while True:
            if money > M:
                break
            money += money * B * 0.01
            ans += 1
        print(ans)
    except EOFError:
        break