n, var = input().split()
if n == "1":
    print(var)
    snake = ""
    for c in var:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    print(snake)
    print(var[0].upper() + var[1:])
elif n == "2":
    print(var[0] + var.title().replace("_", "")[1:])
    print(var)
    print(var.title().replace("_", ""))
elif n == "3":
    print(var[0].lower() + var[1:])
    snake = var[0].lower()
    for c in var[1:]:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    print(snake)
    print(var)