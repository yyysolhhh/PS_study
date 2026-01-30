v, w, d = map(int, input().split())
count = 0
t = w / v

s = 5.0 * t ** 2

while s < d:

    count += 1    

    t *= 1.25  

    s += 5.0 * t ** 2

print(count)