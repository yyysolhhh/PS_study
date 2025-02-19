while True:
    try:
        A, B, C = map(int, input().split())
        ans = max(C - B, B - A) - 1
        print(ans)
    except EOFError:
        break