while True:
    nums = input()
    if nums == "0":
        break
    b, p, m = nums.split()
    b = int(b)
    n = int(p, b) % int(m, b)
    if n == 0:
        print("0")
        continue
    res = []
    while n > 0:
        res.append(str(n % b))
        n //= b
    print(''.join(res[::-1]))