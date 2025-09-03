N = int(input())
A = list(map(int, input().split()))
print("Alice" if N & 1 == 0 else "Bob")