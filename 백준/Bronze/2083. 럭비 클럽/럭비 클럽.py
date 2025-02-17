while True:
    raw = input()
    if raw == "# 0 0":
        break
    name, age, weight = raw.split()
    print(name, "Senior" if int(age) > 17 or int(weight) >= 80 else "Junior")