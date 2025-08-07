def calculate(op, num):
    if op == "@":
        return num * 3
    elif op == "%":
        return num + 5
    elif op == "#":
        return num - 7

T = int(input())
for _ in range(T):
    exp = list(input().split())
    ans = float(exp[0])
    for i in exp[1:]:
        ans = calculate(i, ans)
    print(f"{ans:.2f}")