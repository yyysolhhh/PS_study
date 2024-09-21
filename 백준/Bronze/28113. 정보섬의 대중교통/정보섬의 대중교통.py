N, A, B = map(int, input().split())
if A == B:
    print("Anything")
else:
    print("Bus" if B > A else "Subway")