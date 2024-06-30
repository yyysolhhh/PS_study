import sys
from datetime import datetime, timedelta

input = sys.stdin.readline
N = int(input())

if N == 0:
    print(0)
else:
    dates = []
    l = []
    denominator = 0
    numerator = 0

    for _ in range(N):
        temp = input().split()
        year, month, day = map(int, temp[0].split('/'))
        hour, minute, second = map(int, temp[1].split(':'))
        l.append(int(temp[2]))
        dates.append(datetime(year, month, day, hour, minute, second))

    tn = dates[-1]
    for i in range(len(dates)):
        time_diff = (tn - dates[i]) / timedelta(days=365)
        pi = max(0.5 ** time_diff, 0.9 ** (N - i - 1))
        numerator += pi * l[i]
        denominator += pi

    print(round(numerator / denominator))