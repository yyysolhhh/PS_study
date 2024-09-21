N, A, B = map(int, input().split())
if B == A:
    print("Anything")
else:
    print("Bus" if B > A else "Subway")