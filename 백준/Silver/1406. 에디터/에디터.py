import sys
string = list(sys.stdin.readline().strip())
stack = []
N = len(string)
M = int(sys.stdin.readline())
for _ in range(M):
    command = sys.stdin.readline()
    if command[0] == "L":
        if string:
            stack.append(string.pop())
    elif command[0] == "D":
        if stack:
            string.append(stack.pop())
    elif command[0] == "B":
        if string:
            string.pop()
    elif command[0] == "P":
        string.append(command[2])
print("".join(string + list(reversed(stack))))
