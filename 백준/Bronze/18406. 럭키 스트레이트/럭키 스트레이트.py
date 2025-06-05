N = input()
mid = len(N) // 2
l = sum(map(int, N[:mid]))
r = sum(map(int, N[mid:]))
print("LUCKY" if l == r else "READY")