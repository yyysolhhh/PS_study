n = int(input())
directions = list(map(int, input().split()))
ans = sum(directions)
if ans > 0:
    print("Right")
elif ans < 0:
    print("Left")
else:
    print("Stay")