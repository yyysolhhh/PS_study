from itertools import permutations
n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
ans = set()
for i in permutations(cards, k):
    ans.add("".join(i))
print(len(ans))