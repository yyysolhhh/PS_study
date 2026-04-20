T = int(input())
scores = list(map(int, input().split()))
scores += [0] * 5
if scores[0] > scores[2]:
    n1 = (scores[0] - scores[2]) * 508
else:
    n1 = (scores[2] - scores[0]) * 108
if scores[1] > scores[3]:
    n2 = (scores[1] - scores[3]) * 212
else:
    n2 = (scores[3] - scores[1]) * 305
n3 = scores[4] * 707
ans = (n1 + n2 + n3) * 4763
print(ans)
