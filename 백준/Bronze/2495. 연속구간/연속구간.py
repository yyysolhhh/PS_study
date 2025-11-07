for _ in range(3):
    num = input()
    ans = 1
    temp = 1
    for i in range(1, 8):
        if num[i] == num[i - 1]:
            temp += 1
        else:
            temp = 1
        ans = max(ans, temp)
    print(ans)