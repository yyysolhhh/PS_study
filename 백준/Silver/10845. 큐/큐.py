import sys


def push(x):
    # queue.append(x)
    queue.insert(0, x)


def pop():
    if not queue:
        return -1
    else:
        # return queue.pop(0)
        return queue.pop()


def size():
    return len(queue)


def empty():
    if queue:
        return 0
    else:
        return 1


def front():
    if queue:
        return queue[-1]
    else:
        return -1


def back():
    if queue:
        return queue[0]
    else:
        return -1


N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        x = command[1]
        push(x)
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())
