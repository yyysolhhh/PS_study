ISBN = input()
m_idx = ISBN.index("*")
m = 0
for i in range(len(ISBN)):
    if i == m_idx:
        continue
    weight = 1 if i % 2 == 0 else 3
    m += int(ISBN[i]) * weight
for i in range(10):
    weight = 1 if m_idx % 2 == 0 else 3
    if (m + i * weight) % 10 == 0:
        print(i)
        break