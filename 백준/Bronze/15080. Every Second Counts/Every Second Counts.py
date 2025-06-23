h1, m1, s1 = map(int, input().split(" : "))
h2, m2, s2 = map(int, input().split(" : "))
t1 = 3600 * h1 + 60 * m1 + s1
t2 = 3600 * h2 + 60 * m2 + s2
if t1 > t2:
    print((24 * 3600 + t2) - t1)
else:
    print(t2 - t1)