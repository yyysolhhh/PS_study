def solve(x, y):
    tri = 250 ** 2 / 2
    if x == 0 and y == 0:
        return 125, 125
    elif x > 0 and y > 0:
        if x > y:
            return 0, 250 - tri / x
        else:
            return 250 - tri / y, 0
    elif x == 0 and y < 125:
        temp = tri / (250 - y)
        return temp, 250 - temp
    elif x < 125 and y == 0:
        temp = tri / (250 - x)
        return 250 - temp, temp
    elif x >= 125 and y == 0:
        return 0, tri / x
    elif x == 0 and y >= 125:
        return tri / y, 0
    

a, b = map(int, input().split())
ans_x, ans_y = solve(a, b)
print(f"{ans_x:.2f} {ans_y:.2f}")