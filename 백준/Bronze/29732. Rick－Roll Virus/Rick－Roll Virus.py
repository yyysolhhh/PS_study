import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
S = list(input().strip())
rpp = []
S = ["0"] + S
for i in range(1, N + 1):
    if S[i] == "R":
        rpp.append(i)
for i in rpp:
    for j in range(max(1, i - K), min(N, i + K) + 1):
        S[j] = "R"
if S.count("R") <= M:
    print("Yes")
else:
    print("No")
