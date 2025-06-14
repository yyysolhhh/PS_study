while True:
    try:
        n = list(map(int, input().split()))
        diff = [0]
        ans = "Jolly"
        for i in range(1, n[0]):
            diff.append(abs(n[i + 1] - n[i]))
        diff.sort()
        for i in range(1, n[0]):
            if diff[i] != i:
                ans = "Not jolly"
        print(ans)
    except EOFError:
        break