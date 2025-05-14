N = int(input())
trophy = [int(input()) for _ in range(N)]
l, r = 1, 1
l_max = trophy[0]
for i in trophy:
    if l_max < i:
        l_max = i
        l += 1
r_max = trophy[-1]
for i in trophy[::-1]:
    if r_max < i:
        r_max = i
        r += 1
print(l)
print(r)