n = int(input())
k = int(input())
if n - k >= 60:
    print((k + 60) * 1500 + (n - k - 60) * 3000)
else:
    print(n * 1500)