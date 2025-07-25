import sys
input = sys.stdin.readline

while True:
    maxNum = 10
    minNum = 1
    while True:
        n = int(input().strip())
        if n == 0:
            break
        ans = input().strip()
        if ans == 'right on':
            if n >= minNum and n <= maxNum:
                result = 'Stan may be honest'
            else:
                result = 'Stan is dishonest'
            break
        elif ans == "too high":
            maxNum = min(maxNum, n-1)
        elif ans == "too low":
            minNum = max(minNum, n+1)
    if n == 0:
        break
    print(result)