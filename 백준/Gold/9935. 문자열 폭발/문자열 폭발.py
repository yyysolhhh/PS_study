import sys
input = sys.stdin.readline
string = input().strip()
bomb = input().strip()
stack = []
for i in string:
    stack.append(i)
    if (stack[-1] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb):
        del stack[-len(bomb):]
if stack == []:
    print("FRULA")
else:
    print(''.join(stack))