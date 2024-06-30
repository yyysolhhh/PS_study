from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    is_error = 0
    r = 0
    if n == 0:
        arr = deque()
    for i in p:
        if i == 'R':
            r += 1
        elif i == 'D':
            if len(arr) == 0:
                is_error = 1
                break
            elif r % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    if r % 2 == 1:
        arr.reverse()
    if is_error == 1:
        print("error")
    else:
        print('[' + ','.join(map(str, arr)) + ']')