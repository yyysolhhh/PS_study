A, B, C = map(int, input().split())
I, J, K = map(int, input().split())
x = min(A / I, B / J, C / K)
print(A - I * x, B - J * x, C - K * x)