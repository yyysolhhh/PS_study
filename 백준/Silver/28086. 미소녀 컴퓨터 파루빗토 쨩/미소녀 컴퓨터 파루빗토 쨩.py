import re

def solve(a, b, op):
    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        if b == 0:
            print("invalid")
            return
        res = a // b
    print(oct(res).replace("0o", ""))

form = input()
A, B = "", ""
op_reg = r"[\+\-\*\/]"
flag = True
for i in range(1, len(form)):
    if re.match(op_reg, form[i]):
        op = form[i]
        A = form[:i]
        B = form[i + 1:]
        break
solve(int(A, 8), int(B, 8), op)