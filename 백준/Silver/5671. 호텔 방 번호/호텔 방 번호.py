while True:
    try:
        N, M = map(int, input().split())
        ans = 0
        for i in range(N, M + 1):
            digit = [False for _ in range(10)]
            flag = True
            for j in str(i):
                if not digit[int(j)]:
                    digit[int(j)] = True
                else:
                    flag = False
                    break
            if flag:
                ans += 1
        print(ans)
    except EOFError:
        break