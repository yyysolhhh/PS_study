import sys
input = sys.stdin.readline
while True:
    string = input().rstrip()
    result = "yes"
    if string == '.':
        break
    stack = []
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
                break
    if stack:
      result = 'no'
    print(result)