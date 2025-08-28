import math
A, P1 = map(int, input().split())
R, P2 = map(int, input().split())
whole = math.pi * R ** 2
if P1 / A < P2 / whole:
    print("Slice of pizza")
else:
    print("Whole pizza")