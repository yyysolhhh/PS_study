T = int(input())
for _ in range(T):
    digit = [0 for _ in range(11)]
    X = input()
    for i in X:
        digit[int(i)] = 1
    print(digit.count(1))