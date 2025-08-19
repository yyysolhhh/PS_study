import sys
input = sys.stdin.readline

def rotate(tri):
    rot = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1):
            rot[i][j] = tri[N - 1 - j][i - j]
    return rot
    

def symmetry(tri):
    sym = [[0 for _ in range(N)] for _ in range(N)]
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1):
            sym[i][j] = A[i][i - j]
    return sym

def calculate(ta, tb):
    cnt = 0
    for i in range(N):
        for j in range(i + 1):
            if ta[i][j] != tb[i][j]:
                cnt += 1
    return cnt

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize
for _ in range(3):
    ans = min(ans, calculate(A, B))
    A = rotate(A)
A = symmetry(A)
for _ in range(3):
    ans = min(ans, calculate(A, B))
    A = rotate(A)
print(ans)