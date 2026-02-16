A, B, C = map(int, input().split())
if A == B == C:
    print("*")
elif A == B:
    print("C")
elif A == C:
    print("B")
else:
    print("A")