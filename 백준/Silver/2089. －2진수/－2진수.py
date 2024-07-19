import sys
N = int(sys.stdin.readline())
remainder = ''
if not N:
    sys.stdout.write('0')
    exit()
while N:
    if N % (-2):
        remainder += '1'
        N = N // -2 + 1
    else:
        remainder += '0'
        N //= -2
sys.stdout.write(remainder[::-1])