T, S = map(int, input().split())
if 11 < T <= 16:
    if S == 0:
        print(320)
    else:
        print(280)
else:
    print(280)