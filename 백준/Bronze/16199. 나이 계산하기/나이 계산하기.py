y1, m1, d1 = list(map(int, input().split()))
y2, m2, d2 = list(map(int, input().split()))
yeon = y2 - y1 
se = yeon + 1
if m1 < m2 or (m1 == m2 and d1 <= d2):
    man = yeon
else:
    man = yeon - 1
print(man)
print(se)
print(yeon)
