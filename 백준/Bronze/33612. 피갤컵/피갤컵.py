N = int(input()) - 1
year, mon = 2024, 8
time = mon + N * 7
new_y = year + (time - 1) // 12
new_m = (time - 1) % 12 + 1
print(new_y, new_m)