from collections import Counter
N, M = map(int, input().split())
X = Counter(map(int, input().split()))
print(max(X.values()))