import sys
input = sys.stdin.readline
while True:
    a0 = input().strip()
    if a0 == "0":
        break
    n = len(a0)
    a = [a0]
    while True:
        ai = str(int(a[-1]) ** 2).zfill(n * 2)[n // 2:-n // 2]
        if ai in a:
            break
        a.append(ai)
    print(len(a))