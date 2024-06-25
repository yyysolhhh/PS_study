N = int(input())
A = list(map(int, input().split()))
oks = [-1 for _ in range(N)]
stack = [0]
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        oks[stack.pop()] = A[i]
    stack.append(i)
print(*oks)
