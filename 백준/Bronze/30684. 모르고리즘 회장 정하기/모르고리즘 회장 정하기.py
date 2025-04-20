N = int(input())
candidate = []
for _ in range(N):
    name = input()
    if len(name) == 3:
        candidate.append(name)
print(sorted(candidate)[0])