from collections import deque
import sys
def bfs(A):
    queue = deque([(A, 0)])
    while queue:
        curr, cnt = queue.popleft()
        if curr == B:
            return cnt
        for i in (curr * 2, int(str(curr) + '1')):
            if A <= i <= B:
                queue.append((i, cnt + 1))
    return (-2)
input = sys.stdin.readline
A, B = map(int, input().split())
print(bfs(A) + 1)