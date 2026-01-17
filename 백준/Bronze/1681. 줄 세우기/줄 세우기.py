N, L = map(int, input().split())
cnt = 0
num = 0
while cnt < N:
    num += 1
    if str(L) in str(num):
        continue
    cnt += 1
print(num)