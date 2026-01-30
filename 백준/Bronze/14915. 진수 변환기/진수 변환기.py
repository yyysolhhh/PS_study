m, n = map(int, input().split())
ans = ""
hexa = "0123456789ABCDEF"
if m == 0:
    ans = "0"
while m > 0:
    ans += hexa[m % n]
    m //= n
print(ans[::-1])