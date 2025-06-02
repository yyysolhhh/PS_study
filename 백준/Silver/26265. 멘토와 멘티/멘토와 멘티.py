N = int(input())
pair = []
for _ in range(N):
    pair.append(input().split())
pair.sort(key=lambda x: x[1], reverse=True)
pair.sort(key=lambda x: x[0])
for i, j in pair:
    print(i, j)