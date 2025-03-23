N = int(input())
house = list(map(int, input().split()))
print(sorted(house)[(N - 1) // 2])