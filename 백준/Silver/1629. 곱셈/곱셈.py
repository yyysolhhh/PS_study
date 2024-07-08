import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def DnC(a, b):
    if b == 1:
        return a % C
    temp = DnC(a, b//2)
    if b % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * a % C
A, B, C = map(int, input().split())
print(DnC(A, B))