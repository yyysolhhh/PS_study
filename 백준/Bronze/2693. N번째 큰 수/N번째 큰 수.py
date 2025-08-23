T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    print(sorted(A)[-3])