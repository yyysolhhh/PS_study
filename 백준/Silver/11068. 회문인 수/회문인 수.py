import sys

def decimal_to_base(decimal, base):
    rest_list = []

    while 0 < decimal:
        rest_list.append(decimal % base)
        decimal = decimal // base

    return rest_list

def is_palindrome_list(li):
    return 1 if li == li[::-1] else 0

T = int(sys.stdin.readline())

for _ in range(T):
    number = int(sys.stdin.readline())

    is_palindrome = False

    for i in range(2, 64 + 1):
        
        if is_palindrome_list(decimal_to_base(number, i)):
            is_palindrome = True
            break
    
    if is_palindrome:
        print(1)
    else:
        print(0)