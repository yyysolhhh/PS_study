import sys
T = int(sys.stdin.readline())
for _ in range(T):
    sentence = list(sys.stdin.readline().split())
    for word in sentence:
        for i in range(len(word), 0, -1):
            print(word[i-1], end='')
        print(" ", end='')
