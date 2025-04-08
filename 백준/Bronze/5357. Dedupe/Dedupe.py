t = int(input())
for _ in range(t):
    data = input()
    print(data[0], end="")
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            continue
        print(data[i], end="")
    print()