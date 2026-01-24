import sys
input = sys.stdin.readline
words = []
ans = "Correct"
while True:
    new = input().strip()
    if new == "#":
        if not words:
            break
        else:
            print(ans)
            words = []
            ans = "Correct"
            continue
    words.append(new)
    if len(words) > 1:
        if len(words[-1]) != len(words[-2]):
            ans = "Incorrect"
            continue
        cnt = 0
        for i, j in zip(words[-1], words[-2]):
            if i != j:
                cnt += 1
        if cnt != 1:
            ans = "Incorrect"