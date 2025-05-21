A, B, C = map(int, input().split())
T = int(input())
if T <= 30:
    print(A)
else:
    ex = T - 30
    if ex % B != 0:
        print(A + (ex // B + 1) * C)
    else:
        print(A + ex // B * C)