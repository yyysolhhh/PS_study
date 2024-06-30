S = input()
stack = []
len = 0
for i, c in enumerate(S):
    if c == '(':
        stack.append((int(S[i - 1]), len - 1))
        len = 0
    elif c == ')':
        K, Q = stack.pop()
        len = len * K + Q
    elif c.isdigit():
        len += 1
print(len)