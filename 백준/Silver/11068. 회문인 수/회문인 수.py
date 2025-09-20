import sys
input = sys.stdin.readline

def is_palindrome(n):
    return list(n) == list(reversed(n))

def decimal_to_base(decimal, base):
    base_num = []
    while decimal > 0:
        base_num.append(decimal % base)
        decimal //= base
    return base_num


T = int(input())
for _ in range(T):
    num = input().strip()
    if is_palindrome(num):
        print(1)
        continue
    for i in range(2, 65):
        res = decimal_to_base(int(num), i)
        if is_palindrome(res):
            print(1)
            break
    else:
        print(0)