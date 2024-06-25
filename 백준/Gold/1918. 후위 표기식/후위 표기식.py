infix = input()
stack = []
postfix = []
for i in infix:
    if i.isalpha():
        postfix.append(i)
    else:
        if i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                postfix.append(stack.pop())
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
while stack:
    postfix.append(stack.pop())
print(''.join(postfix))
