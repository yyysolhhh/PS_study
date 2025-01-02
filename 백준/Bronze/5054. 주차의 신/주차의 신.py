t = int(input())
for _ in range(t):
    n = int(input())
    stores = sorted(map(int, input().split()))
    print(2 * (max(stores) - min(stores)))