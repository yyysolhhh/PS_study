import sys
input = sys.stdin.readline

def win_game(Hmax, Hatk):
    Hcur = Hmax
    for t, a, h in rooms:
        if t == 1:
            times = h // Hatk if h % Hatk == 0 else h // Hatk + 1
            Hcur -= a * (times - 1)
        elif t == 2:
            Hcur += h
            Hatk += a
            Hcur = min(Hcur, Hmax)
            if Hcur > Hmax:
                Hcur = Hmax
        if Hcur <= 0:
            return False
    return True

def binary(Hatk):
    result = 0
    left, right = 0, sys.maxsize
    while left <= right:
        mid = (left + right) // 2
        if win_game(mid, Hatk):
            right = mid - 1
            result = mid
        else:
            left = mid + 1
    return result

N, Hatk = map(int, input().split())
rooms = [tuple(map(int, input().split())) for _ in range(N)]
print(binary(Hatk))