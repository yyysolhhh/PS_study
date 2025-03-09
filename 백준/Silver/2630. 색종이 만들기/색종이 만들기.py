import sys
input = sys.stdin.readline

def solve(x, y, size):
    global blue, white
    cnt = sum(sum(paper[i][y:y + size]) for i in range(x, x + size))
    if cnt == 0:
        white += 1
    elif cnt == size * size:
        blue += 1
    else:
        solve(x, y, size // 2)
        solve(x + size // 2, y, size // 2)
        solve(x, y + size // 2, size // 2)
        solve(x + size // 2, y + size // 2, size // 2)
    if size == 1:
        return

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0
solve(0, 0, N)
print(white)
print(blue)