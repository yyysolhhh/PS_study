T = int(input())
for _ in range(T):
    num1 = input()
    num2 = input()
    ans = 0
    for i, j in zip(num1, num2):
        ans += i != j
    print(f"Hamming distance is {ans}.")