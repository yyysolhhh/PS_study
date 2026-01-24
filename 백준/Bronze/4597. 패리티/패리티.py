while True:
    bit = input()
    if bit == "#":
        break
    t = bit[-1]
    bit = bit[:-1]
    cnt = bit.count("1")
    if cnt & 1 == 0:
        if t == "e":
            bit += "0"
        else:
            bit += "1"
    else:
        if t == "e":
            bit += "1"
        else:
            bit += "0"
    print(bit)