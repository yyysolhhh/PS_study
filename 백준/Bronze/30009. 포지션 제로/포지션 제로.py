N = int(input())
X, Y, R = map(int, input().split())
A, B = 0, 0
left = X - R
right = X + R
for _ in range(N):
    T = int(input())
    if left < T < right:
        A += 1
    elif left == T or right == T:
        B += 1
print(A, B)