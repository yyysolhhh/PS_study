import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pack_price = []
unit_price = []
result = 0
for _ in range(M):
    pack, unit = map(int, input().split())
    pack_price.append(pack)
    unit_price.append(unit)
pack_price.sort()
unit_price.sort()
result = min(pack_price[0] * (N // 6) + unit_price[0] * (N % 6), pack_price[0] * (N // 6 + 1), unit_price[0] * N)
print(result) 
