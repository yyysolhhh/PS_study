import sys
def push_front(x):
    deque.insert(0, x)
def push_back(x):
    deque.append(x)
def pop_front():
    if deque:
        return deque.pop(0)
    else:
        return -1
def pop_back():
    if deque:
        return deque.pop()
    else:
        return -1
def size():
    return len(deque)
def empty():
    if deque:
        return 0
    else:
        return 1
def front():
    if deque:
        return deque[0]
    else:
        return -1
def back():
    if deque:
        return deque[-1]
    else:
        return -1
N = int(sys.stdin.readline())
deque = []
for _ in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "push_front":
        x = command[1]
        push_front(x)
    elif command[0] == "push_back":
        x = command[1]
        push_back(x)
    elif command[0] == "pop_front":
        print(pop_front())
    elif command[0] == "pop_back":
        print(pop_back())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())

