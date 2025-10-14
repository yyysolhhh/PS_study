S = input()
for i in S:
    dig = ord(i)
    tot = sum(int(j) for j in str(dig))
    print(i * tot)