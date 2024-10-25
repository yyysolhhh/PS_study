ISBN = input()
missing_index = ISBN.index('*')
m = 0
for i in range(12):
    if i == missing_index:
        continue
    digit = int(ISBN[i])
    weight = 1 if i % 2 == 0 else 3
    m += digit * weight
for x in range(10):
    weight = 1 if missing_index % 2 == 0 else 3
    check_sum = m + x * weight
    if (check_sum + int(ISBN[-1])) % 10 == 0:
        print(x)
        break