N = int(input())
a = sorted(map(int, input().split()))
sung = sum(a[:N // 2])
print(sung, sum(a) - sung)
