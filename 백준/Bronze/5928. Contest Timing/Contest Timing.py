D, H, M = map(int, input().split())
if D < 11:
    print(-1)
elif D == 11 and H < 11:
    print(-1)
elif D == 11 and H == 11 and M < 11:
    print(-1)
else:
    total = (D - 11) * 24 * 60 + (H - 11) * 60 + M - 11
    print(total)