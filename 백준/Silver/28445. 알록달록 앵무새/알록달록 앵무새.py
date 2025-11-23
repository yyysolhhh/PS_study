colors = []
colors.extend(input().split())
colors.extend(input().split())
pair = set()
for i in colors:
    for j in colors:
        pair.add((i, j))
for i, j in sorted(pair):
    print(i, j)