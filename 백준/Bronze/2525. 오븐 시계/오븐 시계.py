A, B = map(int, input().split())
C = int(input())
total_min = A * 60 + B + C
h = (total_min // 60) % 24
m = total_min % 60
print(h, m)