import sys
input = sys.stdin.readline
N, K = map(int, input().split())
scores = []
for _ in range(N):
    scores.append(float(input()))
scores.sort()
adjusted = scores[K] * K + scores[N - K - 1] * K
trimmed = 0
for i in range(K, N - K):
    adjusted += scores[i]
    trimmed += scores[i]
trimmed /= N - 2 * K
adjusted /= N
print("{:.2f}".format(trimmed + 1e-8))
print(f"{adjusted + 1e-8:.2f}")