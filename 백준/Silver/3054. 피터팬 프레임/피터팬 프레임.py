l = input()
wendy, peter = "*", "#"
first = ""
second = ""
third = ""
for i, j in enumerate(l, start=1):
    frame, left = peter, peter
    if i % 3 == 0:
        frame, left = wendy, wendy
    if (i - 1) % 3 == 0 and i != 1:
        left = wendy
    first += f"..{frame}."
    second += f".{frame}.{frame}"
    third += f"{left}.{j}."
first += "."
second += "."
third += frame
print(first)
print(second)
print(third)
print(second)
print(first)