K, N = map(int, input().split())
length = []
for _ in range(K):
    length.append(int(input()))
length.sort()
short = length[-1]
start = 1
end = short
while start <= end:
    num = 0
    measure = (start + end) // 2
    for i in length:
        num += i // measure
    if num >= N:
        start = measure + 1
    else:
        end = measure - 1
print(end)
