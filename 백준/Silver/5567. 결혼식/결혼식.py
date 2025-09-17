from collections import deque
n = int(input())
m = int(input())
rel = [[] for _ in range(n + 1)]
check = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)
q = deque([1])
check[1] = 1
while q: 
    cur = q.popleft()
    for i in rel[cur]:
        if check[i] > 0:
            continue
        check[i] = check[cur] + 1
        q.append(i)
print(sum(1 for i in check if i == 2 or i == 3))