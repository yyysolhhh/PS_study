A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
X = A * P
Y = B + max(0, (P - C) * D)
print(min(X, Y))
