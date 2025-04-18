N, M = map(int, input().split())
for _ in range(N):
    shape = input()
    print(''.join(reversed(shape)))