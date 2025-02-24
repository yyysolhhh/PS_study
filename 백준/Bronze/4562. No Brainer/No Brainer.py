n = int(input())
for _ in range(n):
    X, Y = map(int, input().split())
    print("NO BRAINS" if X < Y else "MMM BRAINS")