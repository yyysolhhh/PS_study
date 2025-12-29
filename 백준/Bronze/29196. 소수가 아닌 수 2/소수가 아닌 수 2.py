k = float(input())
p, q = 1, 1
while abs(p / q - k) > 1e-6:
    if p / q < k:
        p += 1
    else:
        q += 1
print("YES")
print(p, q)