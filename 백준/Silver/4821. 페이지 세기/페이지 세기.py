import sys
input = sys.stdin.readline
while True:
    pages = int(input())
    if pages == 0:
        break
    check = [False for _ in range(pages + 1)]
    ranges = input().split(",")
    for r in ranges:
        if "-" in r:
            low, high = map(int, r.split("-"))
            for i in range(low, high + 1):
                if i > pages:
                    continue
                check[i] = True
        else:
            r = int(r)
            if r > pages:
                continue
            check[r] = True
    print(check.count(True))