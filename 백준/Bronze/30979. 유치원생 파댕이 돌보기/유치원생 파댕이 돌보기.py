T = int(input())
N = int(input())
F = map(int, input().split())
if sum(F) >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")