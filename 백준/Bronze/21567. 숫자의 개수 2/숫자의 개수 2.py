A = int(input())
B = int(input())
C = int(input())
res = A * B * C
for i in range(10):
    print(str(res).count(str(i)))