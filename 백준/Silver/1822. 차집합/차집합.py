nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
ans = A - B
print(len(ans))
print(*sorted(ans))