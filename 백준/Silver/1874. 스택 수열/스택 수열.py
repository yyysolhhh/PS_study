n = int(input())
stack = []
operation = []
count = 0
no = 0
for i in range(n):
    num = int(input())
    while count < num:
        count += 1
        operation.append("+")
        stack.append(count)
    if stack[-1] == num:
        operation.append("-")
        stack.pop()
    else:
        no = True
        break
if no == True:
    print("NO")
else:
    for i in operation:
        print(i)