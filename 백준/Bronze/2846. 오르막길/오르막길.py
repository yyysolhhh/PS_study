N = int(input())
P = list(map(int, input().split()))
h = []
temp = 0
for i in range(1, N):
    if P[i - 1] < P[i]:
        temp += P[i] - P[i - 1]
    else:
        h.append(temp)
        temp = 0
h.append(temp)
print(max(h))