import sys
input = sys.stdin.readline
N = int(input())
X, Y = 0, 0
for _ in range(N):
    winner = input().strip()
    if winner == "D":
        X += 1
    elif winner == "P":
        Y += 1
    if abs(X - Y) >= 2:
        break
print(f"{X}:{Y}")