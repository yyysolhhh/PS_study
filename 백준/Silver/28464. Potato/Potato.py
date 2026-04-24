N = int(input())
potato = list(map(int, input().split()))

potato.sort()

pack = 0
sung = 0
for i in range(N//2):
    sung += potato[i]
pack = sum(potato) - sung

print(sung, pack)