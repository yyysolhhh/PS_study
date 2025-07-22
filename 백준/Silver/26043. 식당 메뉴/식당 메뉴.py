import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
A, B, C = [], [], []
for _ in range(n):
    info = list(map(int, input().split()))
    if info[0] == 1:
        q.append((info[1], info[2]))
    elif info[0] == 2:
        st, menu = q.popleft()
        if menu == info[1]:
            A.append(st)
        else:
            B.append(st)
while q:
    C.append(q.pop()[0])
def print_num(arr):
    if arr:
        print(*sorted(arr))
    else:
        print(None)
print_num(A)
print_num(B)
print_num(C)