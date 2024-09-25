import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
deq = deque()
for i in range(1, N + 1):
    deq.append(i)
while (len(deq) > 1):
    print(deq.popleft(), end=' ')
    deq.append(deq.popleft())
print(deq.pop())